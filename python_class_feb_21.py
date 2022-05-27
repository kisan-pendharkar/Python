##class sagar:
##    
##    def __init__(self,name,age):
##            
##        self.name=name
##        self.age=age
##        print(self.name)
##        print(self.age)
##
##        
##    
##ql=sagar("sagar",23)
##ql.mr

### single inheritance
##class Netzwerk:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##
##    def fun(self):
##        print("hii ",self.name)
##
##class two(Netzwerk): #single inheritance
##    def new(self):
##        print("Your age ",self.age)
##
##obj=two("sagar",12)
##obj.new()
##obj.fun()


##class Netzwerk:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##
##    def fun(self):
##        print("hii ",self.name)
##
##class two(Netzwerk):
##    def __init__(self,age):
##        self.age=age
##        Netzwerk.__init__("sagar",self.age)
##    def new(self):
##        print("Your age ",self.age)
##
##obj=two(30)
##obj.new()
##obj.fun()


# super() method to call imedite parent class using super() method
class Netzwerk:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun(self):
        print("hii ",self.name)

class two(Netzwerk):
    def __init__(self,age):
        self.age=age
        super().__init__("sagar",self.age)
    def new(self):
        print("Your age ",self.age)

obj=two(28)
obj.new()







