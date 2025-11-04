#Checks if number given is actually even    
def even_number_checker(number_to_check):
        if number_to_check % 2 == 0:
           print("The number is even")
        else:
           print("The number is odd")

# Builds the multiplication table
def multiplication_table_generator(table_lenth):
        # Adding 1 to the table length for correct printing
        table_lenth = table_lenth + 1
        for first_num in range(1,(table_lenth)):
         for num in range(1,table_lenth):
           print(f"{first_num} x {num} = {(first_num * num)}")
        #Adding the next line for good visualls
         print("-" * 15)

#Count to the number_to_reach but skipps even numbers
def number_counter(number_to_reach):
        for number in range(number_to_reach):
           if number % 2 == 0:
              continue    
           print(number)
menu = "1.Check if a number is even or odd.\n2.Generate a multiplication table (1 - 5).\n3.Count from 1–10 but skip even numbers.\n4.Exit\nPlease Pick one option: "
def user_utility_console():
#Checks if user wants to exit the program   
 while True:
    user_selection = (input(menu))
    if user_selection == "1":
        user_number = int(input("What number do you want to check for? "))
        even_number_checker(user_number)
            

    elif user_selection == "2":
        user_table_number = int(input("How many multiplication tables would you like: "))
        multiplication_table_generator(user_table_number)
            
    elif user_selection == "3":
        number_to_count = int(input("How many numbers shall I count to: "))
        number_counter(number_to_count)
           
    elif user_selection == "4":
        print("Program Exiting")
        
           
    elif user_selection == "":
        print("Please give input")
        user_selection = (input(menu))
    else:
        print("Invalid Input")
        user_selection = (input(menu))
        
user_utility_console()