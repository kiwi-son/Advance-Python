def decorator(func):
    def wrapper():
        print("I am about to execute a function")
        func()
        print("I have executed this function")
    return wrapper
@decorator
def say():
    print("Hello!")

say()
"""f=decorator(say)
f()"""


