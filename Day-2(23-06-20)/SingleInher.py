class ClassA:
    a,b=20,40
    def display():
        return "I am from ClassA"
    def add(a,b):
        return a+b

class ClassB(ClassA):
    a,b,c=10,20,30
    def show():
        return "I am from ClassB"
    def sub(a,b):
        return a+b

    
