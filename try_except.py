try:
    num = int(input("Enter a number: "))
    result = 10 / num
#If you give zero as input then it will give ZeroDivisionError
#If you give string then it will give value error
except:
    print("You can't divide by zero!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a number.")

try:
    num = int(input("Enter a number: "))
    print(num)
except Exception as e:
    print("Some error occurred!", e)

a=int(input("Enter a numbe 1:"))
b=int(input("Enter a numbe 2:"))
if b==0:
    raise ValueError("Please don't divide 0")
