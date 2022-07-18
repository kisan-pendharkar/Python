import re
var=input("enter mail id  : ")
if re.match(r'[A-Za-z0-9]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',var):
    print("validate email")
else:
    print("invalid email")
