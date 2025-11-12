try:
    a = 345/10
except Exception as e:
    print(e)

#Gets executed when there is no error in try
else:
    print("Hey I am good")

a=int(input("Enter a numbe 1:"))
b=int(input("Enter a numbe 2:"))
try:
    c=a/b
    print(c)
except Exception as e:
    print(e)

#Gets executed all time no matter if try completely exceutes or not
finally:
    print("Hey I am good")