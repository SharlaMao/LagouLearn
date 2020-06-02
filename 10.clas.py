# class Person():
#     self.name = "nonmae"

#     def get_name(self):
#         return self.name;

# print(Person.name)

# p = Person()
# print(p.name)
# print(p.get_name())

# p.name = "lili"
# print(p.name)

# Person.name = "mm"
# print(Person.name)

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name : {self.name},age:{self.age},gender:{self.gender}")

    def drink(self):
        print(f"name : {self.name},age:{self.age},gender:{self.gender}")

    def run(self):
        print(f"name : {self.name}, age : {self.age},gender:{self.gender}")

xx = Person("xx",10,"male")
xr = Person("xr",20,"female")

print(xx.name)
xx.run()

print(xr.name)
xr.run()