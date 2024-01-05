''' 
Project Bike Rental System using OOPs concept
1) Display the total Stock of bikes
2) User can request the bike and total quantity should be added which calculates the total payment
   If a person rent 3 bikes and per bike costs is 1000 so, the user needs to pay 3000 for 3 bikes
3) Tell the rest of bikes that are in stock so that, if the user is interested then he will rent it more accordingly
'''

class Bike_cart():                                          #created a class named Bike_cart
    def __init__(self,stock):                               #constructor which passed the value of stocks
        self.stock = stock
        
    def Display_total_bikes(self):                          #class method 1) it displays the total number of bikes that is passed through the class Bike_cart()
        print(f"The total bikes are {self.stock}")
        
    def Rent_bikes(self,quantity):                          #class method 2) the conceptual part through which a user passes the quantity as per their need
        if quantity<=0:     
            print("Enter the positive value! and let's try again")
        elif quantity>self.stock:
            print("There is less stock available of bikes")
        else:                                                           #main concept of class method which is executed
            print(f"Total Price =  {quantity*1000}")                    # per bike costs 1000 
            print(f"The total bikes left in stock = {self.stock-quantity}")     # left of bike stock available
        
while True:                                                             #using loop
    bike = Bike_cart(100)                                               # calling the class through object name bike
    user_choice= int(input('''
                           1. Display Stock
                           2. Rent a bike 
                           3. Exit
                           '''))
    if user_choice == 1:
        bike.Display_total_bikes()                              #class method 1 called
    elif user_choice == 2:
        count = int(input("Enter the quantity: "))
        bike.Rent_bikes(count)                                  #class method 2 called while passing the quantity of bikes
    elif user_choice == 3:                  
        print("Thank you for using the bike rental program !")      # user satisified and exit the loop
        break
    else:
        print("Invalid Output")