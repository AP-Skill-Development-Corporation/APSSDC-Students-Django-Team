class Student:
    #this class gives info about the Student
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        return {'name':self.name,'rollno':self.rollno}
    

        
        
