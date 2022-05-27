##class Sales:
##    
##    def __init__ (self,id):
##        self.id=id
##        id=100
##
##
##val=Sales(123)
##print(val.id)


##s = "\t\tWelcome\n"  #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove
##print(s.strip())

##class Person:
##    def __init__(self,id):
##        self.id=id
##
##sam=Person(100)
##sam.__dict__["age"]=49
##print(sam.age+len(sam.__dict__))

##class A:
##    def __init__(self,i=0):   # Class B inherits A, but the data field “i” in A is not inherited.
##        self.i=i
##
##class B(A):
##    def __init__(self,j=0):
##        self.j=j
##
##def main():
##    b=B()
##    print(b.i)
##    print(b.j)
##
##main()



##class A:
##    def __init__(self):
##        self.calcI(30)
##        print("i from A is", self.i)
##
##    def calcI(self, i):
##        self.i = 2 * i;
##
##class B(A):
##    def __init__(self):
##        super().__init__()
##        
##    def calcI(self, i):
##        self.i = 3 * i;
##
##b = B()

##def sayHello():
##    print('Hello world!')
##
##sayHello()
##sayHello()


##x=50
##def func(x):
##    print('x is',x)
##    x=2
##    print('changed local x to',x)
##
##func(x)
##print('x ix now',x)

##x=50
##def func():
##    global x
##    print('x is',x)
##    x=2
##    print('changed local x to',x)
##
##func()
##print('value of x is ',x)

##def say(message,time=1):
##    print(message*time)
##
##say("Hello")
##say("Hello",5)

##def func(a,b=5,c=10):
##    print('a is',a,'and b is',b,'and c is',c)
##
##func(3,7)
##func(25,c=24)
##func(c=50,a=100)

##def maximum(x,y):
##    if x>y:
##        return x
##    elif x==y:
##        return 'The number are equal'
##    else:
##        return y
##
##print(maximum(2,3))

##def C2F(c):
##    return c*9/5+32
##
##print(C2F(100))
##print(C2F(0))

##def power(x,y=2):
##    r=1
##    for i in range(y):
##        r=r*x
##    return r
##
##print(power(3))
##print(power(3,3))


##def sum(*args):
##    '''Function returns the sum
##        of all values'''
##    r=0
##    for i in args:
##        r=r+i
##    return r
##
##print(sum.__doc__)
##print(sum(1,2,3))
##print(sum(1,2,3,4,5))

##class A:
##    def __init__(self):
##        self.__i=1
##        self.j=5
##
##    def display(self):
##        print(self.__i,self.j)
##
##class B(A):
##    def __init__(self):
##        super().__init__()
##        self.__i=2
##        self.__j=7
##
##c=B()
##c.display()


##class A:
##    def __init__(self,x):
##        self.x = x
##    def count(self,x):
##        self.x = self.x+1
##class B(A):
##    def __init__(self, y=0):
##        A.__init__(self, 3)
##        self.y = y
##    def count(self):
##        self.y += 1     
##def main():
##    obj = B()
##    obj.count()
##    print(obj.x, obj.y)
##
##main()
##
##
##class A:
##	pass
##class B(A):
##	pass
##obj=B()
##print(isinstance(obj,A))

##class A:
##    def __init__(self):
##        self.__x = 1
##class B(A):
##    def display(self):
##        print(self.__x)
##def main():
##    obj = B()
##    obj.display()
##
##print(main())

##class A:
##    def __init__(self):
##        self._x = 5       
##class B(A):
##    def display(self):
##        print(self._x)
##def main():
##    obj = B()
##    obj.display()
##print(main())

##class A:
##    def test1(self):
##        print(" test of A called ")
##class B(A):
##        def test(self):
##            print(" test of B called ")
##class C(A):
##    def test(self):
##        print(" test of C called ")
##class D(B,C):
##    def test2(self):
##        print(" test of D called ")        
##obj=D()
##obj.test()

##class A:
##    def test(self):
##        print("test of A called")
##class B(A):
##    def test(self):
##        print("test of B called")
##        super().test()  
##class C(A):
##    def test(self):
##        print("test of C called")
##        super().test()
##class D(B,C):
##    def test2(self):
##        print("test of D called")      
##obj=D()
##obj.test()

##class test:
##     def __init__(self,a="Hello World"):
##         self.a=a
## 
##     def display(self):
##         print(self.a)
##obj=test()
##obj.display()

##class change:
##    def __init__(self, x, y, z):
##        self.a = x + y + z
## 
##x = change(1,2,3)
##y = getattr(x, 'a')
##setattr(x, 'a', y+1)
##print(x.a)

##class test:
##    def __init__(self,a):
##        self.a=a
## 
##    def display(self):
##        print(self.a)
##obj=test()
##obj.display()

##class A:
##    def __init__(self,b):
##        self.b=b
##    def display(self):
##        print(self.b)
##obj=A("Hello")
##del obj

##class test:
##    def __init__(self):
##        self.variable = 'Old'
##        self.Change(self.variable)
##    def Change(self, var):
##        var = 'New'
##obj=test()
##print(obj.variable)


class fruits:
    def __init__(self, price):
        self.price = price
obj=fruits(50)
 
obj.quantity=10
obj.bags=2
 
print(obj.quantity+len(obj.__dict__))



class Demo:
    def __init__(self):
        pass
 
    def test(self):
        print(__name__)
 
obj = Demo()
obj.test()





















