class emp:
    company="HPL" #class attribute
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def print_info(self):
        info= f"The name is {self.name} and salary is {self.salary}"
        print(info)
    @staticmethod
    def sum(a,b): #here we don't need to pass self
        return a+b
    @classmethod
    def company_name(cls):
        print(cls.company)
    @classmethod
    def change_compnay(cls,comp): #it's actually class variable not instance variable
        cls.company=comp
e1=emp("Jeet",200)
e2=emp("Sreejit",300)
e1.print_info()
e2.print_info()
print(e2.sum(2,3))
print(emp.sum(2,3))#we can call it using class name

print(e1.company)
e1.change_compnay("Global")
print(e1.company)
print(e2.company)