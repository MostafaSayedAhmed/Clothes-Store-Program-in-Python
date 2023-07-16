# Customer Class Section
# Line 3 : used to import ABC and abstractmethod which are used in abstract class such ass Class Customer
from  abc import ABC,abstractmethod
class Customer(ABC) :
    # Line 6 -11 : Constructor used to initialize class members
    def __init__(self,name,age,money,ID):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__ID=ID
        self.__shopping_list = []
   # Line 13 - 15 : abstract method which will be overwrited in RegularCustomer and Special Customer class
    @abstractmethod
    def buy_clothes(self):
        pass
    # Line 17 - 18 : function used to set money
    def set_money(self,money):
        self.__money = money
    # Line 20 - 21 : function used to get money
    def get_money(self):
        return self.__money
    # Line 23 - 24 : function used to get shopping list
    def set_shoppingList(self,clothe):
        self.__shopping_list.append(clothe)
    # Line 26 - 27 : function used to set shopping list
    def get_shoppingList(self):
        return self.__shopping_list
    # Line 29 - 30 : function used to get name
    def get_name(self):
        return self.__name
    # Line 32 - 33 : function used to set name
    def set_name(self,name):
        self.__name =name
    # Line 35 - 36 : function used to get age
    def get_age(self):
        return self.__age
    # Line 38 - 39 : function used to set age
    def set_age(self,age):
        self.__age = age
    # Line 41 - 42 : function used to get ID
    def get_id(self):
        return int(self.__ID)