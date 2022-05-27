##file_obj=open("sagar.txt","w")
##file_obj.write("Hello sagu")
##file_obj.close()

##file_obj=open(r"C:\Users\Sagar Guttal\Desktop\Python class\sagar1.txt","w")
##file_obj.write("india")
##file_obj.close()

##import tkinter #GUI,Frames,Button,Labels
##from tkinter import filedialog
##import os

##folder =filedialog.askdirectory()
##print(folder)
##
##file=os.path.join(folder,"sagar2.txt")
##file_obj=open(file,"w")
##file_obj.write("Hello sagu i love u")
##file_obj.close()

##file=open("sagar.txt","a")
##file.write("\n")
##file.write("learn python")
##file.close

import tkinter #GUI,Frames,Button,Labels
from tkinter import filedialog
import os

root=tkinter.Tk()
root.withdraw()

folder=filedialog.askdirectory()
print(folder)

file=os.path.join(folder,"sagar.txt")

file_obj=open(file,"a")
file_obj.write("\n")
file_obj.write("ashok and rekha")
file_obj.close()























