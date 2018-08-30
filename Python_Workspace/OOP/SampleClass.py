class SampleClass:
    'This is sample class'                      # Here we write the class documentation
    id = 0                                      # This is a static variable
    __hiddenAttr = 'hidden'                     # Hidden class attribute, prefixed by double underscore
    def __init__(self):
        SampleClass.id = SampleClass.id + 1     # Static is accessed by class name
    
    def __del__(self):                          # Destructor
        print('In destructor')
    
    def display(self):
        print('This is a sample class. Id count ', SampleClass.id)


""" This is 
How we write
Multiline comment in Python """


# Accessing class attributes
obj1 = SampleClass()                            # Creating instance of class
obj2 = SampleClass()
print(SampleClass.id)
obj1.display()                                  # Accessing method of class

# print(obj1.__hiddenAttr)    this will give error
print(obj1._SampleClass__hiddenAttr)