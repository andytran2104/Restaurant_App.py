# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 07:21:51 2022

@author: mgabi
"""

import datetime
import random

# random.randint(0, 9999)
# datetime.now()


class RestaurantApp:
    def __init__(self):
        self.profiles = [] # set as empty at initialization
        self.foodmenu = [] #set food menu as empty at initialization
        self.drinkmenu = []
        self.bill_total = 0
        self.online = False
        self.selfpickup = False
        self.homedelivery = False
        self.all_dine_in = {}
        self.all_pickup = {}
        self.all_delivery = {}
        self.CONST_DINE_IN = "Dine In"
        self.CONST_PICKUP = "Self Pickup"
        self.CONST_DELIVERY = "Home Delivery"
        self.CONST_TITLE_DATE = "Date"
        self.CONST_TITLE_ORDER = "Order ID"
        self.CONST_TITLE_TYPE = "Type of Order"
        self.CONST_TITLE_AMOUNT = "Order Amount"
        self.list_temp = []
        self.list_temp.append(self.CONST_TITLE_DATE)
        self.list_temp.append(self.CONST_TITLE_ORDER)
        self.list_temp.append(self.CONST_TITLE_TYPE)
        self.list_temp.append(self.CONST_TITLE_AMOUNT)
        for item in self.list_temp:
            self.all_dine_in[item] = []
            self.all_pickup[item] = []
            self.all_delivery[item] = []
        
        
    def addCustomer(self,customer):
        self.profiles.append(customer)
    
    def addFood(self, food_list):
         self.foodmenu.extend(food_list)        
    def addDrink(self,drink_list):
         self.drinkmenu.extend(drink_list)
   
    def loginCustomer(self):
        login_attempt=0
        while(login_attempt != 3): # three chances
            uname=input("Please enter your username (mobile number) ")
            pwd= input("Please enter your password ")
            for customer in self.profiles:
                if customer.mobile_number == uname:
                    if customer.password == pwd:
                        print("You have successfully signed in ")
                        print("Welcome " + customer.name)
                        return customer # return the Customer object
                    else: 
                        print("You are unauthorised")
                        print("Password is incorrect")
            login_attempt += 1 # plus 1
        return False
    
    def printStats(self):
        print("Please Enter the option to Print the statistics")
        while(True):
            print("1. All Dine in Orders")
            print("2. All Pick up Orders")
            print("3. All Delivery Orders")
            print("4. Total Amount Spent on All Orders")
            print("5. To go to Previous Menu")
            choice = input()
            if choice == "5":
                return
            menu_str = ""
            for item in self.list_temp:
                menu_str = menu_str + item + str("\t")
            print(menu_str)
            if choice == "1":
                #print(self.all_dine_in)
                for i in range(len(self.all_dine_in[self.CONST_TITLE_DATE])):
                    print(str(self.all_dine_in[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_AMOUNT][i]) + "\t")
            if choice == "2":
                #print(self.all_pickup)
                for i in range(len(self.all_pickup[self.CONST_TITLE_DATE])):
                    print(str(self.all_pickup[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_AMOUNT][i]) + "\t")
            if choice == "3":
                #print(self.all_delivery)
                for i in range(len(self.all_delivery[self.CONST_TITLE_DATE])):
                    print(str(self.all_delivery[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_AMOUNT][i]) + "\t")
            if choice == "4":
                #print("All Orders")
                total_amount = 0
                for i in range(len(self.all_dine_in[self.CONST_TITLE_DATE])):
                    print(str(self.all_dine_in[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_dine_in[self.CONST_TITLE_AMOUNT][i]) + "\t")
                    total_amount = total_amount + self.all_dine_in[self.CONST_TITLE_AMOUNT][i]
                for i in range(len(self.all_pickup[self.CONST_TITLE_DATE])):
                    print(str(self.all_pickup[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_pickup[self.CONST_TITLE_AMOUNT][i]) + "\t")
                    total_amount = total_amount + self.all_pickup[self.CONST_TITLE_AMOUNT][i]
                for i in range(len(self.all_delivery[self.CONST_TITLE_DATE])):
                    print(str(self.all_delivery[self.CONST_TITLE_DATE][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_ORDER][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_TYPE][i]) + "\t" + \
                    str(self.all_delivery[self.CONST_TITLE_AMOUNT][i]) + "\t")
                    total_amount = total_amount + self.all_delivery[self.CONST_TITLE_AMOUNT][i]
                print("Total amount on all order: " + str(total_amount))
        
    def customerOrder(self,customer_logged_in):
        print("Current customer logged in:",customer_logged_in.name) # display name
        while (True): # must have another loop here
            print(" Please enter 2.1 to Start Ordering.")
            print(" Please enter 2.2 to Print Statistics.")
            print(" Please enter 2.3 for Logout.")
            choice = input()
            if choice == "2.1":
                print("Ordering..")
                self.Order()
            if choice == "2.2":
                print("Printing Statistics..")
                self.printStats()
            if choice == "2.3":
                break # end the infinite loop
    
    def display_foodmenu(self):
        for i in self.foodmenu:
            i.display()
    def display_drinkmenu(self):
        for i in self.drinkmenu:
            i.display()
   
    
    def Checkout(self):
        while(True):
            print("Please enter Y to proceed to Checkout or")
            print("Enter N to cancel the order")
            choice = input()
            if choice == 'N':
                print("Order is cancelled")
                break
            elif choice == 'Y':
                print('Proceeding to Checkout')
                date_temp = datetime.datetime.now()
                order_id_temp = random.randint(0, 9999)
                if self.online:
                    if self.selfpickup:
                        print("no charges")
                        self.all_pickup[self.CONST_TITLE_DATE].append(date_temp)
                        self.all_pickup[self.CONST_TITLE_ORDER].append(order_id_temp)
                        self.all_pickup[self.CONST_TITLE_TYPE].append(self.CONST_PICKUP)
                        self.all_pickup[self.CONST_TITLE_AMOUNT].append(self.bill_total)
                    else:
                        while(True):
                            inputkm = input("Enter Number of KM to deliver: ")
                            try:
                                if int(inputkm)<=5:
                                    print("Adding cost of AUD5")
                                    self.bill_total = self.bill_total + 5
                                    break
                                elif int(inputkm)>5 and int(inputkm) <=10:
                                    print("Adding cost of AUD10")
                                    self.bill_total = self.bill_total + 10
                                    break
                                elif int(inputkm)>10 and int(inputkm) <=15:
                                    print("Adding cost of AUD15")
                                    self.bill_total = self.bill_total + 15
                                    break
                                else:
                                    print("Cannot Deliver to this distance")
                            except:
                                print("Please enter integer")
                        print("Total Payable Amount is :" + str(self.bill_total))
                        self.all_delivery[self.CONST_TITLE_DATE].append(date_temp)
                        self.all_delivery[self.CONST_TITLE_ORDER].append(order_id_temp)
                        self.all_delivery[self.CONST_TITLE_TYPE].append(self.CONST_DELIVERY)
                        self.all_delivery[self.CONST_TITLE_AMOUNT].append(self.bill_total)
                else:
                    self.bill_total = self.bill_total + 0.15*self.bill_total
                    print("Total Payable Amount is :" + str(self.bill_total))
                    self.all_dine_in[self.CONST_TITLE_DATE].append(date_temp)
                    self.all_dine_in[self.CONST_TITLE_ORDER].append(order_id_temp)
                    self.all_dine_in[self.CONST_TITLE_TYPE].append(self.CONST_DINE_IN)
                    self.all_dine_in[self.CONST_TITLE_AMOUNT].append(self.bill_total)
                break
        while(True):
            print("Please enter Y to confirm the order or N to cnacel")
            choice = input()
            if choice == 'N':
                print("Cancelling the order")
                break
            elif choice == 'Y':
                print("Thank you for the confirmation")
                break
    
    
        
            
    
    def drinkOrder(self):
        while(True):
            print("Drink Menu")
            self.display_drinkmenu()
            print("Enter 4 for Checkout:")
            choice = int(input())
            if choice >=1 and choice <=3:
                self.bill_total = self.bill_total + self.drinkmenu[choice -1].price
                print(self.drinkmenu[choice - 1].name,"is added",
                      "Total is AUD",self.bill_total )
                
            elif choice == 4:
                self.Checkout() 
                break
        
   
    def foodOrder(self, online):
        while(True):
            print("Food Menu")
            self.display_foodmenu()
            if (online == False):
                print("Enter 7 for Drinks Menu")
            else:
                print("Enter 7 for Checkout")
            choice = int(input())
            if choice >= 1 and choice <= 6:
                self.bill_total = self.bill_total + self.foodmenu[choice -1].price
                print(self.foodmenu[choice - 1].name, "is added",
                      "Total is AUD", self.bill_total)
                print()
            elif (online == False) and (choice == 7):
                self.drinkOrder()
                break
            elif (online ==True) and (choice ==7):
                self.Checkout()
                break
    def Order(self):
        while(True):
            self.bill_total = 0
            print("Please enter 1 for Dine in")
            print("Please enter 2 for Order online")
            print("Please enter 3 to go to the Login Page")
            choice = int(input())
            if choice == 1:
                self.online = False
                self.foodOrder(online = False)
                break
            if choice == 2:
                self.online = True
                self.selfpickup = False
                self.homedelivery = False
                self.OnlineOrder()
                break
            if choice == 3:
                self.loginCustomer()
                
    def OnlineOrder(self):
        while(True):
            print("Enter 1 for Self pickup")
            print("Enter 2 for Home delivery")
            print("Enter 3 to go to Previous Menu")
            choice = int(input())
            if choice == 1:
                print("Pickup Menu:")
                self.selfpickup = True
                self.foodOrder(online = True)
                break
            if choice == 2:
                print('Delivery Menu:')
                self.homedelivery = True
                self.foodOrder(online = True)
                break
            if choice == 3:
               self.foodOrder(online = False)
   
                
        
class food:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def display(self):
        print("Enter",self.id,"for",self.name,"Price","AUD",self.price)
food1 = food('1','Noodle', 2)  
food2 = food('2','Sandwich', 4)
food3 = food('3','Dumpling', 6)
food4 = food('4','Muffin', 8)
food5 = food('5','Pasta', 10)
food6 = food('6','Pizza', 20)


class drink:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def display(self):
        print("Enter",self.id,"for",self.name,"Price","AUD",self.price)
drink1 = drink('1','Coffee', 2)
drink2 = drink('2','Colddrink', 4)
drink3 = drink('3','Shake', 6)

class Customer:

    def __init__(self):
        # initialize as Nones at first
        self.name = None
        self.address = None
        self.mobile_number = None
        self.password = None
        self.bday = None
    
    def signUp(self):
        name=input("Please enter your name : ")
        addr = input("Please enter your address or press enter to skip: ") # optional input
        ph = input("Please enter your mobile number : ")
        pwd=input("Please enter your Password : ")
        con_Pwd=input("Please confirm your Password : ")
        dob=input("please Enter your Date of Birth # DD/MM/YYYY (No Space) : ")

        #check phone numbner is correct
        if(ph[0]!=0 and len(ph)!=10): 
            print("You have enter Phone number invalid format")
            print("Please try again:")
            return False
        
        character=['@','#','$']
        result = [ele for ele in character if(ele in pwd)]
        if(result==False):
            print("Password should include @,# or $")
            print("Please try again:")
            return False

        if(pwd!=con_Pwd):
            print("Your password should be same")
            print("Please try again:")
            return False
        
        out=True
        try:
            day, month, year = dob.split('/') 
            # store the datetime object
            bday = datetime.datetime(int(year), int(month), int(day))  
        except ValueError:
            out = False #if not return false
        if(out==False):
            print("Date should be in correct format")
            print("Please try again:")
            return False
        
        # Get the currrent year (much more flexible and will work in the future)
        year_now = datetime.date.today().year
        dob_year = bday.year # get the year from the datetime object
        if((year_now-dob_year)<18):
            print("Your age should be atleast 18 year old")
            print("Please try again:")
            return False

        # storing this in the object itself
        self.name = name
        self.address = addr
        self.mobile_number = ph
        self.password = pwd
        self.bday = bday

        print("You have sussesfully signed up")
        return True


#main body
# creating a RestaurantApp instance
# it will store all the customer profiles

app = RestaurantApp()
    
food1 = food('1','Noodle', 2)  
food2 = food('2','Sandwich', 4)
food3 = food('3','Dumpling', 6)
food4 = food('4','Muffin', 8)
food5 = food('5','Pasta', 10)
food6 = food('6','Pizza', 20)

drink1 = drink('1','Coffee', 2)
drink2 = drink('2','Colddrink', 4)
drink3 = drink('3','Shake',6)

app.addFood([food1,food2,food3,food4,food5,food6])

app.addDrink([drink1,drink2,drink3])


while(True):
    print("Please enter 1 for signup:")
    print("Please enter 2 for login:")
    print("Please enter 3 for exit:")
    choice=input()
  
    if(choice=="1"): 
        user = Customer()
        response = user.signUp()
        if response == True: # if successful
            app.addCustomer(user) # add to restaurant app 
    if(choice=="2"):
        user = app.loginCustomer()
        if user != False: # if not invalid login
            app.customerOrder(user)
        else:
            print("Invalid login attempt. ")
    if(choice=="3"):
        print("Thank you for using the application")
        break
    
   
    
    
    
    






