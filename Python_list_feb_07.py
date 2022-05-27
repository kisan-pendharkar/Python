##x=["a","b","c"]
##print(x)
##
##y=["d","e","f"]
##print(y)
##print(type(x))
##print(type(y))
##
##print(x+y)
##
##x[0]="sagar"
##print(x)
##
##x[0:3]="x","y","z"
##print(x)
##var=[1,2,3,4,5]
##print(dir(var[0]))


#shallow_copy

##a=["sagu","abhi","shri"]
##a=b
##print(a)
##print(b)
##b[0]="sagya"
##print(a)
##print(b)
##
###deep_copy
##a=["sagu","abhi","shri"]
##a=b[:]
##print(a)
##print(b)
##b[0]="sagya"
##print(a)
##print(b)

##var=["a","b","c"]
##var[0]="dhoni"
##print(var)
##
##var=["a","b","c"]
##var.insert(0,"dhoni")
##print(var)

##var=["a","b","c"]
##var.append("dhoni")
##print(var)
##
##var=["a","b","c"]   #TypeError: list.append() takes exactly one argument (2 given)
##var.append("dhoni","kholi")
##print(var)  

##var=["a","b","c"]
##var.append(["dhoni","kholi"])  #but it contains as another list in list
##print(var)

##var=["a","b","c"]
##var.append("dhoni","kholi")  but it also contains tuple
##print(var)

##var=["a","b","c"]
##var.extend(["dhoni","kholi"]) #in extend we can give more items in list
##print(var)

##var=["dhoni","and","cat","apple","goat"]  # it sorted with existing varible
##var.sort()                 
##print(var)

##var=["dhoni","and","cat","apple","goat"]  # it sorted with new varible
##output=sorted(var)                         #but it dont link with existing variable
##print(output)
##print(var)

##var=["dhoni","and","cat","apple","goat"]  # it sorted with existing varible with reverse sorting
##var.sort(reverse=True)                  
##print(var)

##var=["dhoni","and","cat","apple","goat"]  # it sorted with existing varible by items length
##output=sorted(var,key=len)                 
##print(output)

##var=[15,151,56,115,151]  
##var.sort()                 
##print(var)
##
##var=[15,151,56,115,151]  
##var.sort(reverse=True)                 
##print(var)

##var=[15,151,56,115,151]  
##output=sorted(var,reverse=True)                 
##print(var)
##print(output)

##var=["dhoni","and","cat","apple","goat"]
##var.pop()
##print(var)
## 
##var=["dhoni","and","cat","apple","goat"]
##var.pop(3)
##print(var)
##
##var=["dhoni","and","cat","apple","goat"]
##var.remove("and")
##print(var)
##
##var=["dhoni","and","cat","apple","goat"]
##var.clear()
##print(var)
##
##var=["dhoni","and","cat","apple","goat"]
##del var
##print(var)
##
##var=["dhoni","and","cat","apple","goat"]
##del var[1]
##print(var)


##tuples
var=("dhoni","kholi")
print(var)
print(type(var))

var[0]="rohith"     #TypeError: 'tuple' object does not support item assignment
print(var)          #tuple is immutable
































