from typing import List, Optional


class Table:

    def __init__(self, material: str, height: float, width: float):
        """
        Args:
            material: Материал стола.
            height: Высота стола в метрах.
            width: Ширина стола в метрах.

        Raises:
            TypeError: Если material не строка, height или width не числа.
            ValueError: Если height или width не являются положительными значениями.
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть строкой.")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть числом.")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть числом.")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным значением.")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным значением.")

        self.material = material
        self.height = height
        self.width = width

    def get_area(self) -> float:
        """
        Returns:
            Площадь стола в квадратных метрах.

        Examples:
            >>> table = Table("wood", 1.0, 1.5)
            >>> table.get_area()
            1.5
        """
        return self.height * self.width

    def change_height(self, delta_height: float) -> None:
        """
        Args:
            delta_height: Изменение высоты в метрах.

        Raises:
            TypeError: Если delta_height не число.

        Examples:
            >>> table = Table("wood", 1.0, 1.5)
            >>> table.change_height(0.2)
            >>> table.height
            1.2
        """
        if not isinstance(delta_height, (int, float)):
            raise TypeError("Изменение высоты должно быть числом.")
        self.height += delta_height

    def add_items(self, items: Optional[List[str]] = None) -> str:
        """
        Adds a list of items on the table and returns a message

        Args:
           items: a list of items, default is None

        Returns:
            A string describing items on the table

        Examples:
          >>> table = Table("wood", 1.0, 1.5)
          >>> table.add_items(["notebook", "pen"])
          'Items on the table: notebook, pen'
          >>> table.add_items()
          'No items on the table'
        """
        if items is None:
            return "No items on the table"
        else:
            return f"Items on the table: {', '.join(items)}"


class Tree:

    def __init__(self, species: str, age: int, height: float):
        """
        Args:
            species: Вид дерева.
            age: Возраст дерева в годах.
            height: Высота дерева в метрах.
        Raises:
            TypeError: Если species не строка, age не целое число или height не число.
            ValueError: Если age или height не являются положительными значениями.
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом.")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом.")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным значением.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным значением.")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int, height_increment: float = 0.5) -> float:
        """
        Args:
            years: На сколько лет увеличивается возраст дерева.
            height_increment: На сколько метров увеличивается высота дерева за год (по умолчанию 0.5).

        Returns:
            Общая высота дерева после роста.

        Raises:
            TypeError: Если years не целое число.
            ValueError: Если years не является положительным значением.

        Examples:
            >>> tree = Tree("pine", 10, 5.0)
            >>> tree.grow(5)
            7.5
        """
        if not isinstance(years, int):
            raise TypeError("Возраст должен быть целым числом.")
        if years <= 0:
            raise ValueError("Возраст должен быть положительным значением.")

        self.age += years
        self.height += years * height_increment
        return self.height

    def get_carbon_storage(self, carbon_factor: float) -> float:
        """
        Args:
          carbon_factor: a factor that allows to calculate the amount of carbon storage

        Returns:
          Amount of carbon storage

        Raises:
          TypeError: if carbon_factor is not a float
          ValueError: if carbon_factor is not positive

        Examples:
           >>> tree = Tree("oak", 50, 20.0)
           >>> tree.get_carbon_storage(1.2)
           24.0
        """
        if not isinstance(carbon_factor, (int, float)):
            raise TypeError("Фактор должен быть числом.")
        if carbon_factor <= 0:
            raise ValueError("Фактор должен быть положительным значением.")
        return carbon_factor * self.height

    def get_age_and_species(self) -> str:
        """
        Returns:
          Formatted string with age and species

        Examples:
          >>> tree = Tree("oak", 50, 20.0)
          >>> tree.get_age_and_species()
          'Species: oak, age: 50 years'
        """
        return f"Species: {self.species}, age: {self.age} years"


class Facebook:

    def __init__(self, name: str, users: int, is_active: bool):
        """
        Args:
            name: Название социальной сети.
            users: Количество пользователей социальной сети.
            is_active: Активна ли социальная сеть.
        Raises:
            TypeError: Если name не строка или users не целое число
            ValueError: Если users не является положительным значением
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой.")
        if not isinstance(users, int):
            raise TypeError("Количество пользователей социальной сети должно быть целым числом.")
        if users <= 0:
            raise ValueError("Количество пользователей социальной сети должно быть положительным значением")
        self.name = name
        self.users = users
        self.is_active = is_active

    def add_users(self, count: int) -> None:
        """
        Args:
            count: Количество новых пользователей.

        Raises:
            TypeError: Если count не целое число.
            ValueError: Если count не является положительным значением.
        """
        if not isinstance(count, int):
            raise TypeError("Количество пользователей должно быть целым числом.")
        if count <= 0:
            raise ValueError("Количество пользователей должно быть положительным значением.")
        self.users += count

    def get_active_status(self) -> bool:
        """
          Returns:
            True if network is active
            False otherwise
          Examples:
              >>> fb = Facebook("Facebook", 100000, True)
              >>> fb.get_active_status()
              True
          """
        return self.is_active

    def change_status(self, new_status: bool = True) -> None:
        """
          Args:
              new_status: new status to set, default is True
          Examples:
            >>> fb = Facebook("Facebook", 100000, True)
            >>> fb.change_status(False)
            >>> fb.is_active
            False
          """
        self.is_active = new_status


if __name__ == "__main__":
    import doctest

    doctest.testmod()
