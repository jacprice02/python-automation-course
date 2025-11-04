#Day 2 - Learnt about python variables and string manipulation
def day2():
  def simple_calculator():
     print("\n--- Simple Calculator ---")
     a = float(input("Enter the first number: "))
     b = float(input("Enter the second number: "))
     print("\nResults:")
     print(f"{a} + {b} = {a + b}")
     print(f"{a} - {b} = {a - b}")
     print(f"{a} * {b} = {a * b}")
     print(f"{a} / {b} = {a / b}")
  def temperature_converter():
       celsius = float(input("Enter a temperature in celsius:"))
       farhenhiet = celsius * 9/5 + 32
       print(farhenhiet)
  def average_calculator():
       print("Enter three numbers")
       a = float(input("Enter the first number: "))
       b = float(input("Enter the second number: "))
       c = float(input("Enter the last number: "))
       average = (a+b+c)/3  
       print(average)
  average_calculator()   
#Day 3 Conditiona and boolean logic

def day3():
    def smart_assistant():
     print("\n--- Smart Assistant ---")
     name = input("Hello! What’s your name? ")
     mood = input(f"Nice to meet you, {name}. How are you feeling today? ").lower()

     if "sad" in mood or "tired" in mood:
        print("I'm sorry to hear that. Maybe take a short break or a walk?")
     elif "happy" in mood or "good" in mood:
        print("That’s great! Keep that energy going!")
     else:
        print("Thanks for sharing. I hope your day goes well!")
    smart_assistant()        
def day4():
   def task_repeater():
    print("\n--- Task Repeater ---")
    task = input("What task do you want to repeat? ")
    times = int(input("How many times should I repeat it? "))

    for i in range(times):
        print(f"({i + 1}) {task}")
   def password_retry_system():
       password = "trade"
       attempts = 0
       guess = input("Try to guess: ")
       while attempts < 3:
        if guess == password:
             print("Correct")
             break
        elif guess != password:
            attempts += 1
            print(f"wrong you have used {attempts} attempt")
            if attempts == 3:
               print("Accses Denied")
               break
            else:
               guess = input("Try to guess: ")
             
             
   password_retry_system()

def day5():
      def even_number_skipper():
         for number in range(10):
           if number % 2 == 0:
              continue
           elif number == 9:
              break    
           print(number)

      def login_gate():
        USERNAME = "Jacob"
        PASSWORD = 12345
        username = input("Enter the username: ")
        password = int(input("Enter the password: "))

        if USERNAME == username and PASSWORD == password:
           print("Accses granted")
        elif USERNAME == username and PASSWORD != password:
           print("Wrong Password")
        else:
           print("Invalid Credentials")      

      login_gate()


def day6():
   def number_analyzer():
     for num in range(5):
        ask = int(input("Give me a number: "))
        if ask % 2 == 0:
           print("The number you have given me is even")
        if ask % 2 == 1:
           if ask > 10:
              print("The number you have given me is a large odd number")
           if ask < 10:
              print("The number you have given me is a small odd number")
   def multiplication_table():
      for first_num in range(1,6):
         for num in range(1,6):
           print(f"{first_num} x {num} = {(first_num * num)}")

   multiplication_table()

    






day6()