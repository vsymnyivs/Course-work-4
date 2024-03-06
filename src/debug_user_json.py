from src.user_forms import UserForm


class DebugUserJson(UserForm):
    """
    Класс для отлавливания ошибок
    """
    payment = None
    city = None

    def user_input_int(self):
        """
        Проверка на наличие ошибок ввода
        :return: integer
        """
        self.payment = input("Введите минимальную заработную плату: ")
        if self.payment.isalpha():
            raise ValueError("Неверно указана зарплата. Убедитесь, что указано число.")
        if self.payment == "":
            self.payment = 0
        return int(self.payment)

    def user_input_str(self):
        """
        Проверка на наличие ошибок ввода
        :return: string
        """
        self.city = input("Введите желаемый город: ").title()
        if self.city.isdigit():
            raise TypeError("Город не может быть числом")
        return self.city


if __name__ == '__main__':
    r = DebugUserJson()
    print(r.user_input_str())
