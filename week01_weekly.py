#Day 2 - Learnt about python variables and string manipulation
'''When you break code, don’t copy the fix immediately.
Pause 30 seconds and predict why it failed — then test your hypothesis.
This slow debugging reflection multiplies your understanding over time.'''
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

day3()
