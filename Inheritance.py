class Base:
    def base_method(self):
        print("This is method from base class")

class Child(Base):
    def child_method(self):
        print("This is method from child class")

class Grandchild(Child):
    def grandchild_method(self):
        print("This is method from grand child class")


obj1 = Grandchild()
obj1.base_method()
obj1.grandchild_method()
obj1.child_method()
