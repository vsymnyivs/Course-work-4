from abc import ABC, abstractmethod


class UserForm(ABC):
    @abstractmethod
    def user_input_int(self):
        pass

    @abstractmethod
    def user_input_str(self):
        pass
    