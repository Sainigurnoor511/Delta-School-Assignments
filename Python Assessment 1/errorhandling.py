# Error handling example in python
#
# Author: Gurnoor Singh Saini

try:
    x=int(input("Enter a number: "))
    y=int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("An error occurred:", str(e))
else:
    print("No error occurred")
finally:
    print("End of error handling")