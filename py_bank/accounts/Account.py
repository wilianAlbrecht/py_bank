from abc import ABC
from abc import abstractmethod

class Account(ABC):

    def __init__(self, number, agency, balance) -> None:
        self.__number = number
        self.__agency = agency
        self.__balance = balance

    
    @abstractmethod
    def withdraw():
        ...
    