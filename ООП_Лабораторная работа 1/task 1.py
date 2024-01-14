import doctest


class Table:
    def __init__(self, material: str, height: float, amount_of_seats: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param height: Высота стола
        :param amount_of_seats: Количество мест

        Примеры:
        >>> table = Table("дерево", 1.5, 4)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть типа str")
        self.material = material

        if not isinstance(height, float):
            raise TypeError("Высота стола должна быть типа float")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = height

        if not isinstance(amount_of_seats, int):
            raise TypeError("Количество мест должно быть типа int")
        if amount_of_seats <= 0:
            raise ValueError("Количество мест должно быть положительным числом")
        self.amount_of_seats = amount_of_seats

    def add_more_seats(self, seats: int) -> None:
        """
        Добавление мест для сидения.
        :param seats: количество дополнительных мест

        :raise ValueError: Если количество добавляемых мест превышает количество уже имеющихся мест, то вызываем ошибку

        Примеры:
        >>> table = Table("дерево", 1.5, 4)
        >>> table.add_more_seats(3)
        """
        if not isinstance(seats, int):
            raise TypeError("Добавляемые места должны быть типа int")
        if not 0 < seats < self.amount_of_seats:
            raise ValueError("Слишком много мест")
        ...

    def add_height(self, elevation: float) -> None:
        """
        Добавление высоты.
        :param elevation : дополнительная высота

        Примеры:
        >>> table = Table("дерево", 1.5, 4)
        >>> table.add_height(0.5)
        """
        if not isinstance(elevation, float):
            raise TypeError("Дополнительная высота должна быть типа float")
        ...

    def free_seats(self) -> bool:
        """
        Функция которая проверяет есть ли свободные места

        :return: Есть ли свободные места

        Примеры:
        >>> table = Table("дерево", 1.5, 4)
        >>> table.free_seats()
        """
        ...


class VK:
    def __init__(self, name: str, amount_of_users: int):
        """
        Создание и подготовка к работе объекта "VK"

        :param name: Название соцсети
        :param amount_of_users: Количество пользователей соцсети

        Примеры:
        >>> vk = VK("ВКонтакте", 10000000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(amount_of_users, int):
            raise TypeError("Количество пользователей должно быть типа int")
        if amount_of_users <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом")
        self.amount_of_users = amount_of_users

    def delete_fake_users(self, fake_users: int) -> None:
        """
        Удаление фейковых пользователей.
        :param fake_users: количество фейковых пользователей

        :raise ValueError: Если количество фейковых пользователей превышает количество уже имеющихся пользователей,
        то вызываем ошибку

        Примеры:
        >>> vk = VK("ВКонтакте", 10000000)
        >>> vk.delete_fake_users(1568)
        """
        if not isinstance(fake_users, int):
            raise TypeError("Количество фейковых пользователей должно быть типа int")
        if not 0 < fake_users < self.amount_of_users:
            raise ValueError("Слишком много фейковых пользователей")
        ...

    def change_name(self, new_name: str) -> None:
        """
        Изменение названия соцсети.
        :param new_name: новое название

        Примеры:
        >>> vk = VK("ВКонтакте", 10000000)
        >>> vk.change_name("Facebook")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое название должно быть типа str")
        ...


class Computer:
    def __init__(self, name: str, weight: float, processor: str, memory_size: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param name: Наименование компьютера
        :param weight: Количество пользователей соцсети
        :param processor: Наименование процессоро
        :param memory_size: Количество памяти

        Примеры:
        >>> comp = Computer("Lenovo", 1.5, "Intel", 128)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть типа float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

        if not isinstance(processor, str):
            raise TypeError("Название процессора должно быть типа str")
        self.processor = processor

        if not isinstance(memory_size, int):
            raise TypeError("Объем памети должен быть типа int")
        if memory_size <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory_size = memory_size

    def add_memory(self, additional_memory: int) -> None:
        """
        Добавление памяти.
        :param additional_memory: количество памяти

        :raise ValueError: количество памяти должно быть положительным числом

        Примеры:
        >>> comp = Computer("Lenovo", 1.5, "Intel", 128)
        >>> comp.add_memory(64)
        """
        if not isinstance(additional_memory, int):
            raise TypeError("Количество памяти должно быть типа int")
        if additional_memory <= 0:
            raise ValueError("Количество памяти должно быть положительным числом")
        ...

    def change_processor(self, new_processor: str) -> None:
        """
        Изменение процессора.
        :param new_processor: новое название

        Примеры:
        >>> comp = Computer("Lenovo", 1.5, "Intel", 128)
        >>> comp.change_processor("Rysen")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
