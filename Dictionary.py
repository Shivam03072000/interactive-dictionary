import json    #in a json type file, te data is stored as a dictionary in python
import difflib
from difflib import SequenceMatcher  #importing the sequencematcher from difflib module

#create a file object
myfile=open("data.json")
data=json.load(myfile)
wordentered=input("enter the word: ")
word=wordentered.lower()  #so that the search in not case sensitive
f=0
try:
    meaning=data[word]
    print("the meaning is",end=': \n')
    for k in meaning :
        print(k)
except:
    if (word.title() in data.keys()):    #for words like 'Delhi' etc.
        meaning = data[word.title]
        print("the meaning is", end=': \n')
        for k in meaning:
            print(k)
    elif word.upper() in data.keys():    #for words like 'USA', 'NATO' etc.
        meaning = data[word.upper()]
        print("the meaning is", end=': \n')
        for k in meaning:
            print(k)

    else:
        r=[]
        for k in data.keys():
            if(SequenceMatcher(None,word,k).ratio()>.75):   #SequenceMatcher returns an object, then it is converted to float by ratio method
                r.append(k)
                f=1

        if (f == 1):
            for i in range(0,len(r)):
                print('\n')
                print("did you mean",r[i],"instead ?",end=' ')
                answer=input("enter 'y' for yes and 'n' for no")
                t=0
                if(answer is 'y'):
                    print('\n')
                    meaning=data[r[i]]
                    print("the meaning is", end=': \n')
                    for k in meaning:
                        print(k)
                    t=1
                    break

            if(t==0):
                print('\n')
                print("word not found")

        else:
            print("word not found in the dictionary")

