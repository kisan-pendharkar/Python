##class my_work:
##    
##    var="dhoni"
##    age="38"
##    role="batsman"
##    
##    def player_info(self):
##        
##        print(f"{var} is a {role}")
##        
##obj=my_work()
####print(obj.var)
##obj.player_info()

##class Netzwerk:
##
##    var = "dhoni"
##    def fun(self):
##        print(var)
##
##obj=Netzwerk()
##print(obj.var)
##obj.fun()

##class Netzwerk:
##    def __init__(self,name):
##        self.name=name
##
##    def fun(self):
##        print(self.name)
##
##obj=Netzwerk("sagar")
##obj.fun()


input_animal=input("enter animal name :-")
class animal:
    def __init__(self,input_animal):
        self.voice=input_animal

    def dog(self):
        print(self.voice)

obj=animal("bark")
obj.dog()

if obj.dog() != "Dog":
    print("ohhhh fuck you")












        
        
        
