class Alphabet:

    ua_lang = "UA"
    ua_letters = list("абвгґдеєжзийіклмнопрстуфхцчшщьюя")

    def __init__(self, lang: str = ua_lang, letters: list = None):
        if not isinstance(lang, str):
            raise TypeError("lang має бути рядком (str)")
        if not lang:
            raise ValueError("lang не може бути порожнім")

        if letters is None:
            letters = Alphabet.ua_letters
        else:
            if not isinstance(letters, list):
                raise TypeError("letters має бути списком")
            if not letters:
                raise ValueError("letters не може бути порожнім")
            for letter in letters:
                if not isinstance(letter, str):
                    raise TypeError("Кожна літера у letters має бути рядком")
                if len(letter) != 1:
                    raise ValueError(f"'{letter}' не є односимвольним рядком")

        self.lang = lang.upper()
        self.letters = letters

    def print_alphabet(self):
        if not self.letters:
            raise ValueError("Немає літер для виводу")
        print("Алфавіт:", " ".join(self.letters))

    def letters_num(self) -> int:
        if not isinstance(self.letters, list):
            raise TypeError("letters має бути списком")
        return len(self.letters)

    def is_ua_lang(self, text: str) -> bool:

        if not isinstance(text, str):
            raise TypeError("text має бути рядком")

        text = text.lower()

        for ch in text:
            if ch.isalpha() and ch not in Alphabet.ua_letters:
                return False
        return True


class EngAlphabet(Alphabet):


    __en_letters_num = 26

    def __init__(self):
        import string
        english_letters = list(string.ascii_lowercase)

        if len(english_letters) != EngAlphabet.__en_letters_num:
            raise ValueError("Довжина англійського алфавіту повинна бути 26")

        super().__init__("EN", english_letters)

    def is_en_letter(self, letter: str) -> bool:

        if not isinstance(letter, str):
            raise TypeError("letter має бути рядком")
        if len(letter) != 1:
            raise ValueError("letter має бути одним символом")
        if not letter.isalpha():
            return False

        return letter.lower() in self.letters

    def letters_num(self):
        return EngAlphabet.__en_letters_num

    @staticmethod
    def example() -> str:
        return "This is an example sentence in English."


try:
    eng = EngAlphabet()
    eng.print_alphabet()

    print("Кількість букв у англійському алфавіті:", eng.letters_num())
    print("Чи 'H' — англ. літера?", eng.is_en_letter("H"))

    ua = Alphabet()
    print("Чи 'Л' — українська літера?", ua.is_ua_lang("Л"))

    print("Приклад англійського тексту:", EngAlphabet.example())

except Exception as e:
    print("Виникла помилка:", e)
