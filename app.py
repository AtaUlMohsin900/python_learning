# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Your Name is:, {name}! Your age is: {age} years old.")

def greeting():
  return "Hello"
print(greeting())

import datetime
now = datetime.datetime.now()
print(now)

class Greeting:
  def greet(self, name):
    return 'Full Stack Software' + name
print(Greeting().greet(' Developer'))