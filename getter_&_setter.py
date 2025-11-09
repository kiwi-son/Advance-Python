class emp:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    @property
    def first_name(self):
        l=self.name.split(" ")
        return l[0]
    @first_name.setter #@property function name.setter
    def first_name(self,n):
        l = self.name.split(" ")
        new=f"{n} {l[1]}"
        self.name=new


e=emp("Jeet Sadhukhan", "50K")
# print(e.first_name())
# print(e.name)
# e.set_first_name("Rohit")
# print(e.name)
print(e.first_name)
e.first_name="JOHN"
print(e.name)
