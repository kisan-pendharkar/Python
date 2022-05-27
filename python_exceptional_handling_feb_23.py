##var=10/0
##print(var)
 #exception is ZeroDivisionError: division by zero

##try:
##    var=10/0
##    print(var)
##except:
##    print("sorry")
##print("welcome")

##try:
##    var="a"+20
##    print(var)
##except:
##    print("sorry")
##print("welcome")    

##try:
##    var=10/0
##    print(var)
##except TypeError:
##    print("sorry")
##except:
##    print("Oops")
##print("Welcome")

##try:
##    a=10
##    b="sagar"
##    var=a+b
##    print(var)
##except TypeError:
##    print("Opps")


## User can defined error:

##try:
##    var=10
##    if var>5:
##        raise IndexError
##
##except IndexError:
##    print("Oh my error")


##try:
##    var=10
##    if var>5:
##        raise IndexError
##
##except IndexError as ex:
##    print(ex)


##try:
##    var=10
##    if var>5:
##        raise IndexError("Oh my error")
##
##except IndexError as ex:
##    print(ex)

##try:
##    var=10
##    if var>5:
##        raise MyError("oh error") #error code because python doesnot recoinsed Myerror we musr give python errors
##except MyError as ex:
##    print(ex)


## Creating my own error using class

##class Myerror(Exception):
##    pass
##try:
##    var=10
##    if var>5:
##        raise Myerror("oh error")
##
##except Myerror as ex:
##    print(ex)

##class Myerror(Exception):
##    var="oh error"
##try:
##    var=10
##    if var>5:
##        raise Myerror
##
##except Myerror as ex:
##    print(ex.var)

##class Myerror(Exception):
##    var="oh error"
##try:
##    var=10
##    if var>5:
##        raise Myerror("oh error")
##
##except Myerror:
##    print(Myerror.var)






























    


##
