import Car_Bike as cb
import sys
#def Main():
    #test_command = ''
    #while test_command != 'f':
        #test_command = input
    #ans = True
def main():
   menu()
   pass

def menu():
    print("************Welcome to The Garage**************")
    print()
    menuChoice = input("""
        1: Car
        2: Bike
        3: Exit
        Select The Car Type: """)

    if menuChoice == "1":
        Car()
    elif menuChoice == "2":
        Bike()
    elif menuChoice=="3":
        sys.exit
    else:
        print("You've selected an invalild type")
        print("Please try again")
        menu()

def Car(cb):
   pass
    
def Bike():
   pass

if __name__ == '__main__':
    cb.main()