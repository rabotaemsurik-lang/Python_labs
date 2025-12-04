import csv
import os
from statistics import mean
import matplotlib.pyplot as plt

class KmrCsv:
    ref = None    # шлях до csv
    num = None    # номер КМР

    def __init__(self, ref=None, num=None):
        self.data = []

        if ref:
            self.set_ref(ref)
        if num:
            self.set_num(num)

    def set_ref(self, ref: str):
        if not isinstance(ref, str) or not ref.strip():
            raise ValueError("ref має бути непорожнім рядком")
        if not os.path.exists(ref):
            raise FileNotFoundError(f"Файл {ref} не знайдено")
        KmrCsv.ref = ref
        self.ref = ref

    def get_ref(self):
        return self.ref

    def set_num(self, num: int):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("num має бути додатним числом")
        KmrCsv.num = num
        self.num = num

    def read_csv(self):
        if not self.ref:
            raise ValueError("ref не встановлено")
        with open(self.ref, encoding="utf-8") as f:
            reader = csv.reader(f)
            self.data = [row for row in reader]
        return self.data

    def info(self):
        if not self.data:
            raise ValueError("Спочатку виконайте read_csv()")
        print(f"КМР №{self.num}: виконали {len(self.data)} студентів")



class Statistic:

    def avg_stat(self, data):

        if not data:
            raise ValueError("data порожнє")

        questions = len(data[0]) - 3
        res = []

        for q in range(3, 3 + questions):
            correct = sum(int(row[q]) for row in data)
            res.append(100 * correct / len(data))

        return tuple(res)

    def marks_stat(self, data):
        if not data:
            raise ValueError("data порожнє")

        result = {}
        for row in data:
            mark = int(row[1])
            result[mark] = result.get(mark, 0) + 1

        return result

    def marks_per_time(self, data):
        result = {}
        for row in data:
            sid = row[0]
            mark = float(row[1])
            time = float(row[2])
            if time == 0:
                avg = 0
            else:
                avg = mark / (time / 60)  # бал/хв
            result[sid] = avg
        return result

    def best_marks_per_time(self, data, bottom_margin, top_margin):

        res = []

        for row in data:
            total = int(row[1])
            if bottom_margin <= total <= top_margin:
                sid = row[0]
                time = float(row[2])
                avg = total / (time / 60)
                res.append((sid, total, avg))

        res.sort(key=lambda x: x[2], reverse=True)
        return tuple(res[:5])


class Plots:

    def set_cat(self, cat):
        if not os.path.exists(cat):
            os.makedirs(cat)
        self.cat = cat

    def avg_plot(self, avg_tuple):
        plt.figure(figsize=(10,5))
        plt.bar(range(1, len(avg_tuple)+1), avg_tuple)
        plt.xlabel("Питання")
        plt.ylabel("Відсоток правильних відповідей")
        plt.title("Статистика правильних відповідей")
        path = os.path.join(self.cat, "avg_plot.png")
        plt.savefig(path)
        plt.close()
        print(f"avg_plot збережено у {path}")

    def marks_plot(self, marks_dict):
        plt.figure(figsize=(10,5))
        plt.bar(marks_dict.keys(), marks_dict.values())
        plt.xlabel("Оцінки")
        plt.ylabel("Кількість студентів")
        path = os.path.join(self.cat, "marks_plot.png")
        plt.savefig(path)
        plt.close()
        print(f"marks_plot збережено у {path}")

    def best_marks_plot(self, best_tuple):
        ids = [x[0] for x in best_tuple]
        vals = [x[2] for x in best_tuple]
        plt.figure(figsize=(10,5))
        plt.bar(ids, vals)
        plt.xlabel("ID студента")
        plt.ylabel("Бал/хв")
        path = os.path.join(self.cat, "best_marks.png")
        plt.savefig(path)
        plt.close()
        print(f"best_marks_plot збережено у {path}")


class KmrWork(KmrCsv, Statistic, Plots):

    kmrs = {}
    cat = "results"

    def __init__(self, ref, num):
        super().__init__(ref, num)
        KmrWork.kmrs[num] = ref
        self.set_cat(KmrWork.cat)
        self.read_csv()

    def compare_csv(self, other):
        if not isinstance(other, KmrWork):
            raise TypeError("Потрібен інший об'єкт KmrWork")

        # Кількість виконань
        count1 = len(self.data)
        count2 = len(other.data)

        # Середній бал
        avg1 = mean([float(row[1]) for row in self.data])
        avg2 = mean([float(row[1]) for row in other.data])

        # Середній час
        time1 = mean([float(row[2]) for row in self.data])
        time2 = mean([float(row[2]) for row in other.data])

        txt = (
            f"Порівняння КМР {self.num} і {other.num}:\n"
            f"Кількість студентів: {count1} vs {count2}\n"
            f"Середній бал: {avg1:.2f} vs {avg2:.2f}\n"
            f"Середній час: {time1:.2f} vs {time2:.2f}\n"
        )

        print(txt)


        path = os.path.join(self.cat, "compare.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"Результат записано у {path}")

    def compare_avg_plots(self, other):
        avg1 = self.avg_stat(self.data)
        avg2 = other.avg_stat(other.data)

        plt.figure(figsize=(10,5))
        plt.plot(avg1, label=f"КМР {self.num}")
        plt.plot(avg2, label=f"КМР {other.num}")
        plt.legend()
        plt.xlabel("Питання")
        plt.ylabel("Відсоток")
        plt.title("Порівняння правильних відповідей")
        path = os.path.join(self.cat, "compare_avg.png")
        plt.savefig(path)
        plt.close()
        print(f"compare_avg_plots збережено у {path}")
