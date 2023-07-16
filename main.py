"""This program saves information about customer and allow shop owner to view it and modify informatopn about
goods. each customer has an unique id that identify it form other customers. if the customer is new to system
he/she will be asked to give his/her name , age and the current amount of money"""
from Clothes import Clothes
from Tshirt import Tshirt
from Customer import Customer
from RegularCustomer import RegularCustomer
from SpecialCustomer import SpecialCustomer
import random
# Line 11 - 14 : function that calculate the number of the remaining pieces
def remaining_pieces():
    sum1 = trousers.get_number_of_pieces() + tshirtshort.get_number_of_pieces() + tshirtshort.get_number_of_pieces()
    sum2 = jackets.get_number_of_pieces() + shoes.get_number_of_pieces()
    return (sum1 + sum2)
# Line 16 - 19 : function that shows information about the required piece of clothes to the shop owner
def clothes_info (cloth) :
    print("Number of pieces remaining : {}".format(cloth.get_number_of_pieces()))
    print("Material : {}".format(cloth.get_material()))
    print("Price : {}".format(cloth.get_price()))
# Line 21-33 : function used in purchase. it shows information about clothes to customer and make purchase operation
def buy_goods(cloth,name,customerperson):
    inputdial = 0
    print("Here is the information about the available {}".format(name))
    print("The material : {}".format(cloth.get_material()))
    print("The price : {}".format(cloth.get_price()))
    print("Would you like to buy {} ?".format(name))
    inputdial = int(input("Enter 1 for yes or 0 for no : "))
    if (inputdial == 1):
        customerperson.buy_clothes(cloth)
        print("Would you like any other piece of clothes ?")
        inputdial = int(input("Enter 1 for yes or 0 for no : "))
        return inputdial
# Line 35-40 : function used to show all information about customer to customer
def customer_profile(customerpersona):
    print("Here is your profile")
    print("your name is {}".format(customerpersona.get_name()))
    print("your age is {}".format(customerpersona.get_age()))
    print("your ID is {}".format(customerpersona.get_id()))
    print("your current money = {}".format(customerpersona.get_money()))
    print("shopping list = ".format(customerpersona.get_shoppingList()))
# Line 43 - 46 : function used to see if the customer who signed in is in the system or not
def profile_fetching(id,list) :
    for i in list :
        if(id == i.get_id()) :
            return i
# Line 48 - 55 : function used to show information about each customer registered in the system to the shop owner
def list_info(customlist):
    j=1
    for i in customlist:
        print("customer number {} :".format(j))
        print("Name : {} ,age : {} , money : {}".format(i.get_name(),i.get_age(),i.get_money()))
        print("ID : {}".format(i.get_id()))
        print("Shopping list : ")
        for k in i.get_shoppingList() :
            print("  {}  ".format(k.get_name()))
        j+=1
# Line 57 -67 : function used to offer services to shop owner including price editing and adding pieces
def shopowner_services(clothe):
    print("What would you like to edit ?")
    print("Enter 1 for editing price")
    print("Enter 2 for adding pieces")
    inputdial = int(input("Enter number : "))
    if (inputdial == 1):
        newprice = int(input("Enter new price :"))
        clothe.set_price(newprice)
    elif (inputdial == 2):
        pieces = int(input("Enter the additional pieces :"))
        clothe.set_number_of_pieces(pieces)

# ------------ Main ---------------------#
# Line 71 - 75 : initial conditions this conditions can be changed by shop owner
# for number of pieces less than the initial condition use negative number
# for number of pieces more than the initial condition use positive number
tshirtLong = Tshirt(100, "cotton", 50, "long","Long slevee T-shirt")
tshirtshort = Tshirt(100, "cotton", 50, "short","Short slevee T-shirt")
trousers = Clothes(150, "jeans", 60,"Trousers")
jackets = Clothes(200, "leather", 20,"Jackets")
shoes = Clothes(300, "leather", 25,"Shoes")
# Line 79 - 80 : initializing lists one for regular customers and one for special customers
regcustomerList = []
specustomerList = []
# Line 82 : inputdial is a very important variable upon which the rest of program depend
inputdial = 1
# Line 84 : while(1) to ensure the repeation of the program infinite number of times
while (1):
    # Line 86 - 88 : used to welcome the customer/shop owner and asking whether the user is customer or shop owner
    print("Hello sir, How can i help you ?")
    print("Enter 1 for customer")
    print("Enter 2 for shop owner")
    # Line 90 : used to input the number which will move the program to customer section or shop owner section
    inputdial = int(input("Enter the number please : "))
    # Line 92 - 162 : if condition used for customer section
    if (inputdial == 1) :
        print("Hello Dear customer")
        # Line 95 : used to input number which determine which the customer is regular or not
        customerNumber = int(input("For regular customer , enter 1 . for special customer , enter 2 :"))
        # Line 99 - 113 : if condition to sign in or sign up a regular customer
        if (customerNumber == 1):
            id = int(input("Please enter your id (if you don't have one , enter 0) : "))
            obj = profile_fetching(id,regcustomerList)
            if (isinstance(obj,Customer)):
                customer = profile_fetching(id, regcustomerList)
                print("Welcome back mr. {}".format(customer.get_name()))
            else:
                print("Look like you are not in our system")
                name = input("Please, enter your name : ")
                age = int(input("Your age : "))
                money = int(input("And your money : "))
                id = int(random.random() * 10000)
                print("Here is your ID : {}".format(id))
                customer = RegularCustomer(name, age, money, id)
                regcustomerList.append(customer)
        # Line 115 - 129 : if condition to sign in or sign up a special customer
        elif (customerNumber == 2):
            id = input("Please enter your id (if you don't have one , enter 0) : ")
            obj = profile_fetching(id, specustomerList)
            if (isinstance(obj,Customer)):
                customer = profile_fetching(id, specustomerList)
                print("Welcome back mr. {}".format(customer.get_name()))
            else:
                print("Look like you are not in our system")
                name = input("Please, enter your name : ")
                age = int(input("Your age : "))
                money = int(input("And your money : "))
                id = int(random.random() * 10000)
                print("Here is your ID : {}".format(id))
                customer = SpecialCustomer(name, age, money, id)
                specustomerList.append(customer)
        # Line 131 : while statement is useful if customer wanted further services which will be asked when he buy goods
        while(inputdial == 1) :
            print("What would you like to buy")
            print("Enter 1 for buying T-Shirts ")
            print("Enter 2 for buying Trousers ")
            print("Enter 3 for buying Jackets ")
            print("Enter 4 for buying shoes ")
            print("Enter 5 for entering your profile")
            # Line 139 : this line used to enter number corresponding to service that customer demand
            inputdial = int(input("Enter the number please : "))

            if (inputdial == 1):
                print("Would you like to buy a long sleeve T-shirt or short sleeve T-shirt ?")
                inputdial = int(input("1 for long sleeve , 2 for short sleeve : "))
                if (inputdial == 1):
                    inputdial = buy_goods(tshirtLong, "Long sleeve T-shirts", customer)
                elif (inputdial == 2):
                    inputdial = buy_goods(tshirtshort, "Short sleeve T-shirts", customer)
            elif (inputdial == 2):
                inputdial = buy_goods(trousers, "Trousers", customer)
            elif (inputdial == 3):
                inputdial = buy_goods(jackets, "Jacket", customer)
            elif (inputdial == 4):
                inputdial = buy_goods(shoes, "Shoes", customer)
            # Line 155 - 156 : if condition used to display customer profile name , id and age
            elif (inputdial == 5):
                customer_profile(customer)
                inputdial = int(input("if you would like to modify anything , enter 2 : "))
                # Line 159 -173 : if condtion used to allow customer to modify some of his information
                if (inputdial == 2):
                    print("enter 1 to modify your name")
                    print("enter 2 to modify your age")
                    print("enter 3 to modify your current amount of money")
                    inputdial = int(input("Emter number : "))
                    if (inputdial == 1):
                        name = input("Enter the new name : ")
                        customer.set_name(name)
                    elif (inputdial == 2):
                        age = int(input("Enter the new age : "))
                        customer.set_age(age)
                    elif (inputdial == 3):
                        money = int(input("Enter the current amount of money : "))
                        customer.set_money(money)
                inputdial = 1
    # Line 175 - 215 : shop owner services section
    elif (inputdial == 2) :
        # Line 177 - 196 : greeting the owner and showing information about every piece of cloth
       print("Hello shop owner")
       print("Here are information about the remaining goods")
       print("Total number of remaining pieces = {}".format(remaining_pieces()))
       print("Long sleeve T-shirt :")
       clothes_info(tshirtLong)
       print("Short sleeve T-shirt :")
       clothes_info(tshirtshort)
       print("Trousers :")
       clothes_info(trousers)
       print("Jackets :")
       clothes_info(jackets)
       print("Shoes :")
       clothes_info(shoes)
       print("Regular Customers List : ")
       list_info(regcustomerList)
       print("Special Customers List : ")
       list_info(specustomerList)
       print("for reseting the program , enter 1")
       print("for changing info about goods , enter 2")
       inputdial = int(input("Enter number : "))
       # Line 198 - 215 : this section is used to modify any information about the availiable pieces of cloth
       if(inputdial == 2):
           print("Enter 1 for editing T-Shirts ")
           print("Enter 2 for editing Trousers ")
           print("Enter 3 for editing Jackets ")
           print("Enter 4 for editing shoes ")
           inputdial = int(input("Enter number : "))
           if(inputdial == 1):
               inputdial = int(input("1 for long sleeve , 2 for short sleeve : "))
               if(inputdial==1):
                   shopowner_services(tshirtLong)
               elif(inputdial == 2):
                   shopowner_services(tshirtshort)
           elif(inputdial == 2):
               shopowner_services(trousers)
           elif(inputdial == 3):
               shopowner_services(jackets)
           elif(inputdial==4):
               shopowner_services(shoes)
# Note : when modifying number of pieces be aware that you don't change the number of pieces you just add
# for example : if shoes were 50 pieces and you wrote 40 , pieces it will be 90 pieces not 40











