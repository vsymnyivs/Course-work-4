class Vacancy:
    """
    Форма для класса GetHeadHunter
    """
    def __init__(self, name, page):
        """
        Создание экземпляра класса Vacancy
        """
        self.__name = name
        self.__page = page

    @property
    def name(self):
        """
        getter для приватного атрибута name
        """
        return self.__name

    @property
    def page(self):
        """
        getter для приватного атрибута page
        """
        return self.__page

    def __str__(self):
        """
        Магический метод str
        """
        return f"{self.__name}"

    def __repr__(self):
        """
        Магический метод repr
        """
        return f"{self.__class__.__name__}({self.__name, self.__page})"

    @name.setter
    def name(self, value):
        self._name = value

    @page.setter
    def page(self, value):
        self._page = value
