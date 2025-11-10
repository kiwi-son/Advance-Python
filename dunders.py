class emp:
    company="HPL" #class attribute
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}"
    def __len__(self):
        return len(self.name)
e=emp("Jeet",12000)
print(str(e))
print(len(e))

