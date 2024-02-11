class SocialNetwork:
    """
    Базовый класс, описывающий социальную сеть

    Атрибуты:
        number_of_users (int) - Количество пользователей социальной сети
        year_of_creation (int) - Год создания социальной сети
    """

    def __init__(self, number_of_users: int, year_of_creation: int):
        """
        Инициализация класса Social Network

        :param number_of_users: Количество пользователей социальной сети
        :param year_of_creation: Год создания социальной сети
        """
        self._number_of_users = number_of_users
        self._year_of_creation = year_of_creation

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта СоциальнаяСеть.
        """
        return \
            f"Социальная сеть: Год создания: " \
            f"{self._year_of_creation} год, количество пользователей: {self._number_of_users}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта СоциальнаяСеть.
        """
        return \
            f"{self.__class__.__name__}(number_of_users={self._number_of_users!r}, " \
            f"year_of_creation={self._year_of_creation!r}"

    @property
    def number_of_users(self) -> int:
        """
        Геттер для атрибута number_of_users

        Возвращает:
            int: Количество пользователей
        """
        return self._number_of_users

    @number_of_users.setter
    def number_of_users(self, number_of_users: int) -> None:
        """
        Сеттер для атрибута number_of_users

        Аргументы:
            value (int): Новое значение количества пользователей
        """
        if not isinstance(number_of_users, int):
            raise ValueError("Количество пользователей должно быть целым числом")
        if number_of_users <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом")
        self._number_of_users = number_of_users

    @property
    def year_of_creation(self) -> int:
        """
        Геттер для атрибута year_of_creation

        Возвращает:
            int: Год создания
        """
        return self._year_of_creation

    @year_of_creation.setter
    def year_of_creation(self, year_of_creation: int) -> None:
        """
        Сеттер для атрибута year_of_creation

        Аргументы:
            value (int): Новое значение года создания
        """
        if not isinstance(year_of_creation, int):
            raise ValueError("Год создания должен быть целым числом")
        if year_of_creation <= 0:
            raise ValueError("Год создания должен быть положительным числом")
        self._year_of_creation = year_of_creation


class VK(SocialNetwork):
    """
    Дочерний класс, описывающий социальную сеть ВК

    Атрибуты:
        number_of_users (int) - Количество пользователей социальной сети
        year_of_creation (int) - Год основания социальной сети
        founder (str) - Основатель
    """

    def __init__(self, number_of_users: int, year_of_creation: int, founder: str):
        """
        Инициализация дочернего класса VK

        :param number_of_users: Количество пользователей социальной сети
        :param year_of_creation: Год основания социальной сети
        :param founder: Основатель
        """
        super().__init__(number_of_users, year_of_creation)
        self._founder = founder

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта VK.
        """
        return \
            f"Социальная сеть {self.__class__.__name__} Год создания: {self.year_of_creation} год, количество " \
            f"пользователей: {self.number_of_users}, основатель: {self._founder}"
        # Метод перегружен для добавления названия социальной сети и ее основателя

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта VK.
        """
        return \
            f"{self.__class__.__name__}(number_of_users={self.number_of_users!r}, " \
            f"year_of_creation={self.year_of_creation!r}, founder={self._founder})"

    # Метод перегружен для добавления основателя социальной сети

    def add_post(self, id_of_user: int, text: str) -> None:
        """
        Добавляет запись на стену пользователя в ВК.

        :param id_of_user: ID пользователя, добавляющего запись
        :param text: Текст записи

        Возвращает:
            None
        """
        # Реализация: Отправка запроса для добавления записи на стену
        pass

    @property
    def founder(self) -> str:
        """
        Геттер для атрибута founder

        Возвращает:
            str: Имя создателя
        """
        return self._founder

    @founder.setter
    def founder(self, founder: str) -> None:
        """
        Сеттер для атрибута founder

        Аргументы:
            value (str): Новое значение имени создателя
        """
        self._founder = founder

    # Геттеры и сеттера для атрибутов number_of_users и year_of_creation наследуются дочерним классом от базового
