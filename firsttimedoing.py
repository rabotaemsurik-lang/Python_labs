a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))
d = int(input("Введіть d: "))

suma = a + b + c + d
vidnim = a - b
mnozh = c * d
dilennya = c / a
step = a ** b
int_dil = c // a
ost_vid_dil = a % b

print("Додавання a + b + c + d :", suma)
print("Віднімання a - b:", vidnim)
print("Множення c * d:", mnozh)
print("Ділення c / a:", dilennya)
print("Степінь a ** b:", step)
print("Цілочисельне ділення c // a:", int_dil)
print("Остача від ділення a % b:", ost_vid_dil)
print("Виведення списку:")
list_dii = [suma, vidnim, mnozh, dilennya, step, int_dil, ost_vid_dil]
for i in list_dii:
    print(i)
print("К-сть елементів у списку:", len(list_dii))
print("Парні елементи списку:")
for j in list_dii:
    if isinstance(j, int) and j % 2 == 0:
        print(j)
print("Виведення спику, де змінено 2 та 5 елемнти:")
list_dii[1], list_dii[4] = list_dii[4], list_dii[1]
for k in list_dii:
    print(k)

print("ВВедіть ім'я")
name = input()
print("Л.р виконав", name, "студент групи ІПЗ-24-2")
print("Виконані всі завдання")







