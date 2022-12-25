class MainClass():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
    print("Running constructor for JORzClass")
    # Create attributes and set initial values
    self.message = my_greeting
 def my_method(self):
    print(self.message)
    #Object created to call class
main_class1 = MainClass("Morning everyone!")
main_class2 = MainClass("Lets get ready!")
main_class1.my_method()
main_class2.my_method()
print(type(main_class1))
print(type(main_class2))