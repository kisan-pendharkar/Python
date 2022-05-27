class A():
    def fun(self):
        print("a")

class B(A):
    def fun(self):
        print("b")

class C(A):
    def fun(self):
        print("c")

class D(B,C):
    def fun1(self):
        print("d")

d=D()
d.fun()
