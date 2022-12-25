#Class MyClass template
class MainClass:
# __init__ function initiated when class is called
  def __init__(self, studentname, rollnumber):
    self.studentname = studentname
    self.rollnumber = rollnumber
# class method used inside class
  def info(self):
    print("Hello my name is " + self.studentname)
# object a used to call the class and method
a = MainClass("Ajay", "L00170943")
a.info()