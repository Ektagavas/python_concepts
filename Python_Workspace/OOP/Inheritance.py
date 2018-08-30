class Parent:                               # Parent class
    parent_id = 0

    def __init__(self):
        self.parent_id = 4

    def disp(self):
        print('Parent id is ', self.parent_id)


class Child(Parent):                        # Child class
    child_id = 0

    def __init__(self):
        self.child_id = 1

    # Overriding parent class method
    def disp(self):
        # Calling parent class method from child class with same signature
        super().disp()
        print('Child id is ', self.child_id)


obj1 = Child()
# obj1.display()
obj1.disp()
