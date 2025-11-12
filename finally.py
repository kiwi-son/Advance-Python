def divide (a,b):
    try:
        c=a/b
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("Code excuted")

a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2:"))
print(divide(a,b))