class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, first_name):
        new_name = f"{first_name} {self.name.split(" ")[1]}"
        self.name = new_name

e = Employee("John Doe", 50_000)

# print(e.first_name())
#
# e.set_first_name("Smith")
# print(e.name)

print(e.first_name)
e.first_name = "Smith"
print(e.first_name)