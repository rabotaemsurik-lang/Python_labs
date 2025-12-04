class Apple:


    states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]

    def __init__(self, index: int):
        if not isinstance(index, int) or index < 0:
            raise ValueError("index має бути додатним цілим числом")

        self._index = index
        self._state = Apple.states[0]  # початковий стан "Відсутнє"

    def grow(self):

        current_index = Apple.states.index(self._state)
        if current_index < len(Apple.states) - 1:
            self._state = Apple.states[current_index + 1]

    def is_ripe(self):

        return self._state == Apple.states[-1]

    def __str__(self):
        return f"Яблуко {self._index}: {self._state}"



class AppleTree:


    def __init__(self, count: int):
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Кількість яблук має бути додатним цілим числом")

        self.apples = [Apple(i) for i in range(count)]

    def grow_all(self):

        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):

        if not self.apples:
            raise ValueError("Немає яблук на дереві")
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):

        self.apples.clear()

    def __str__(self):
        return "\n".join(str(apple) for apple in self.apples)



class Gardener:


    def __init__(self, name: str, tree: AppleTree):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name має бути непорожнім рядком")
        if not isinstance(tree, AppleTree):
            raise TypeError("tree має бути об'єктом AppleTree")

        self.name = name
        self._tree = tree

    def work(self):

        print(f"\n{self.name} працює... Яблука ростуть!")
        self._tree.grow_all()

    def harvest(self):

        print(f"\n{self.name} перевіряє яблука...")

        if self._tree.all_are_ripe():
            print("Усі яблука стиглі! Збираємо урожай!")
            self._tree.give_away_all()
        else:
            print("Не всі яблука стиглі! Потрібно ще почекати!")

    @staticmethod
    def apple_base(tree: AppleTree):

        if not isinstance(tree, AppleTree):
            raise TypeError("tree має бути об'єктом AppleTree")

        print("\n=== ДОВІДКА ПРО ЯБЛУКА ===")
        if not tree.apples:
            print("На дереві немає яблук!")
            return

        print(f"Кількість яблук: {len(tree.apples)}")
        for apple in tree.apples:
            print(str(apple))
        print("==========================")
