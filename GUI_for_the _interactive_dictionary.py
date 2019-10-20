from tkinter import *
import json
import tkinter.messagebox
import difflib
from difflib import *

dictionary=Tk()  #window created

myfile=open("data.json")
dict=json.load(myfile)

def meaning():

    if (word.get() in dict):
        tx.insert(END,dict[word.get()])

    else:
        r = []     #stores the close words
        for k in dict.keys():
            if (SequenceMatcher(None,word.get(),k).ratio() > .75):  # SequenceMatcher returns an object, then it is converted to float by ratio method
                r.append(k)
                f = 1
        #now the list r[] has the close words stored in it
        flag=0           #tells if the word was found in the list or not

        #print(len(r))
        for i in range(len(r)):
            answer=tkinter.messagebox.askquestion('ERROR','Word not found! Did you mean '+r[i])
            if answer=='yes':
                flag=1
                break

        if flag==0:
            tkinter.messagebox.showinfo('ERROR','Word not found')

        else:
            tx.insert(END,dict[r[i]])

label1=Label(dictionary,text="Word : ")
label1.grid(row=0,column=0)

bt=Button(dictionary,text="Search",command=meaning,fg="blue",bg="yellow")
bt.grid(row=0,column=2)

word=StringVar()
en=Entry(dictionary,textvariable=word)
en.grid(row=0,column=1)

label2=Label(dictionary,text="Meaning : ")
label2.grid(row=1,column=0)

tx=Text(dictionary,height=5,width=40)
tx.grid(row=1,column=1)

dictionary.mainloop()