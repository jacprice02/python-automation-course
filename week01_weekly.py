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

day2()
