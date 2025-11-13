from functools import reduce
num=[1,2,3,45]

# def square(x):
#     return x*x
#
# n= list(map(square, num))

n=list(map(lambda x: x*x, num))


print(n)

def great(x):
    if x>9:
        return True
    else:
        return False

a=[34,67,1,45,2,67,2,89]

n=list(filter(great,a))
print(n)

m=list(filter(lambda x: x>9, a))
print(m)


a=[1,2,3,4,6]
def sum(a,b):
    return a+b
c=reduce(sum, a)
print(c)

