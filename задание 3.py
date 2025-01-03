class Book:

    def __init__(self, name: str, author: str) :
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property  
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self._name}, Автор: {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int) :
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        return f"{super().__str__()} , Страниц: {self._pages}"

    def __repr__(self) -> str:
        return f"PaperBook(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self) -> str:
        return f"{super().__str__()} , Продолжительность: {self._duration}"

    def __repr__(self) -> str:
        return f"AudioBook(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    if __name__ == "__main__":
        book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
        paper_book = PaperBook("Pride and Prejudice", "Jane Austen", 432)
        audio_book = AudioBook("1984", "George Orwell", 11.5)

        print(book)
        print(paper_book)
        print(audio_book)

        print(repr(book))
        print(repr(paper_book))
        print(repr(audio_book))

        try:
            paper_book.pages = -100
        except ValueError as e:
            print(e)

        try:
            paper_book.pages = "abc"
        except TypeError as e:
            print(e)

        try:
            audio_book.duration = -1
        except ValueError as e:
            print(e)

        try:
            audio_book.duration = "abc"
        except TypeError as e:
            print(e)

        try:
            book.name = "new name"
        except AttributeError as e:
            print(e)

        print(f"Name of book: {book.name}")
        print(f"Page number of paper book: {paper_book.pages}")
        print(f"Duration of audio book: {audio_book.duration}")
