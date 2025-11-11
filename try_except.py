try:
    num = int(input("Enter a number: "))
    result = 10 / num
#If you give zero as input then it will give ZeroDivisionError
#If you give string then it will give value error
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")