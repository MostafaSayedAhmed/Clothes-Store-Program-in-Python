# Tshirt Class section as it has 1 additional parameter from clothes class which is sleeve
from Clothes import  Clothes
class Tshirt(Clothes):
    # Line 5 -7 : Constructor which is similar to that of Clothes class but have one additional parameter sleeve
     def __init__(self,price , material , numberofpieces,name,sleeve):
         super().__init__(price , material , numberofpieces,name)
         self.__sleeve = sleeve
     # Line 9 - 10 : function used to set sleeve (actually it isn't used in this program)
     def set_sleeve(self,sleeve):
         self.__sleeve = sleeve
     # Line 12 - 13 : function used to get sleeve
     def get_sleeve(self):
         return self.__sleeve