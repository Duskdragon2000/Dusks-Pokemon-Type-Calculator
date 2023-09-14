import tkinter as tk
import numpy as np
from tkinter import font
from dark_title_bar import *
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = tk.Tk()
dark_title_bar(app)
app.iconbitmap(resource_path('./ball.ico'))
app.title("Pokemon Type Calculator")
app.geometry('1250x875')
app.config(bg="#1e1e1e")

fontOG = tk.font.Font(family="Small Fonts", size=25, weight='bold', underline=True)
dict = {
'typeName': 
['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 
'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']
,
'typeChart': [
[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], # Normal
[1, 0.5, 2, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 0.5, 1], # Fire
[1, 0.5, 0.5, 2, 2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1], # Water
[1, 1, 1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1], # Electric
[1, 2, 0.5, 0.5, 0.5, 2, 1, 2, 0.5, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1], # Grass
[1, 2, 1, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1], # Ice
[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 0.5, 1, 1, 0.5, 1, 2, 1], # Fighting
[1, 1, 1, 1, 0.5, 1, 0.5, 0.5, 2, 1, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1], # Poison
[1, 1, 2, 0, 2, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1], # Ground
[1, 1, 1, 2, 0.5, 2, 0.5, 1, 0, 1, 1, 0.5, 2, 1, 1, 1, 1, 1, 1], # Flying
[1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0.5, 2, 1, 2, 1, 2, 1, 1, 1], # Psychic
[1, 2, 1, 1, 0.5, 1, 0.5, 1, 0.5, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], # Bug
[0.5, 0.5, 2, 1, 2, 1, 2, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1], # Rock
[0, 1, 1, 1, 1, 1, 0, 0.5, 1, 1, 1, 0.5, 1, 2, 1, 2, 1, 1, 1], # Ghost
[1, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1], # Dragon
[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0.5, 1, 0.5, 1, 2, 1], # Dark
[0.5, 2, 1, 1, 0.5, 0.5, 2, 0, 2, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 1, 0.5, 0.5, 1], # Steel
[1, 1, 1, 1, 1, 1, 0.5, 2, 1, 1, 1, 0.5, 1, 1, 0, 0.5, 2, 1, 1], # Fairy
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # None
],
'typeColor':
['#A8A77A','#EE8130','#6390F0','#F7D02C','#7AC74C','#96D9D6','#C22E28','#A33EA1','#E2BF65','#A98FF3'
,'#F95587','#A6B91A','#B6A136','#735797','#6F35FC','#705746','#B7B7CE','#D685AD']
,
'buttons':[]  

}

calcArray = []

class Button:
    def __init__(self, type, weakness, color, number):
        self.type = type
        self.weakness = weakness
        self.color = color
        self.number = number
        self.button = tk.Button(text=self.type, bg= self.color, command= self.click, height=2, width= 8, font=fontOG, activebackground='#1e1e1e')
        
        if self.number >= 0 and self.number <= 5:
            self.button.grid(row= 0, column=self.number, padx= 10, pady=10)

        if self.number >= 6 and self.number <= 11:
            self.button.grid(row= 1, column=self.number-6, padx= 10, pady=10)

        if self.number >= 12 and self.number <= 17:
            self.button.grid(row= 3, column=self.number-12, padx= 10, pady=10)


    def click(self):
        
        calcArray.append(self.weakness)
        self.button.configure(bg = '#1e1e1e', fg= self.button.cget('bg'), relief= 'sunken', command= self.unclick)

        #print('calcArray ', calcArray)

        if len(calcArray) == 2:
            for x in range(len(dict['typeName'])):
                if dict['typeChart'][x] not in calcArray:
                    #print("x is", dict['typeName'][x])
                    dict['buttons'][x].button.configure(state = 'disabled')


            # multiply selected types (1 type mults none) (2 types mult eachother)
        if len(calcArray) == 1:

            mulAnswer = np.multiply(calcArray[0], dict['typeChart'][18])
            outputStr(mulAnswer)

        if len(calcArray) == 2:

            mulAnswer = np.multiply(calcArray[0], calcArray[1])
            outputStr(mulAnswer)

        
                    
                    
    def unclick(self):
        #print(self.type, " unclicked")
        calcArray.remove(self.weakness)
        self.button.configure(bg = self.button.cget('fg'), fg= '#000000' , relief= 'raised', command= self.click)

        #print('calcArray ', calcArray)

        for x in range(len(dict['typeName'])):
                dict['buttons'][x].button.configure(state = 'normal')
                
        if len(calcArray) == 0:
            typeText.configure(text= "No Types Selected") 

        if len(calcArray) == 1:

            mulAnswer = np.multiply(calcArray[0], dict['typeChart'][18])
            outputStr(mulAnswer)

        if len(calcArray) == 2:

            mulAnswer = np.multiply(calcArray[0], calcArray[1])
            outputStr(mulAnswer)

        

def outputStr(array):
    
    global typesSelected

    #make arrays two sort the effectivness of types
    fourx=[]
    twox=[]
    onex=[]
    halfx=[]
    quarterx=[]
    zerox=[]
    final='\n\n'

    #Sort types into the array
    for x in range(len(array)-1):
        match array[x]:
            case 4.0:
                fourx.append(dict['typeName'][x])
            case 2.0:
                twox.append(dict['typeName'][x])
            case 1.0:
                onex.append(dict['typeName'][x])
            case 0.5:
                halfx.append(dict['typeName'][x])
            case 0.25:
                quarterx.append(dict['typeName'][x])
            case 0.0:
                zerox.append(dict['typeName'][x])

    #FOUR TIMES
    if len(fourx) > 0:

        final= final + ("Takes 4x from: ")

        for x in range(len(fourx)):
            final = final + "[" + fourx[x] + "]  "
        
        final= final + "\n\n"

    #TWO TIMES
    if len(twox) > 0:

        final= final + "Takes 2x from: "

        for x in range(len(twox)):
            final = final + "[" + twox[x] + "] "
        
        final= final + "\n\n"

    #ONE TIMES 
    if len(onex) > 0:

        final= final + "Takes 1x from: "

        for x in range(len(onex)):
            final = final + "[" + onex[x] + "] "
        
        final= final + "\n\n"
    
    #HALF TIMES
    if len(halfx) > 0:

        final= final + "Takes 1 /2x from: "

        for x in range(len(halfx)):
            final = final + "[" + halfx[x] + "] "
        
        final= final + "\n\n"
    
    #QUARTER TIMES 
    if len(quarterx) > 0:

        final= final + "Takes 1 /4x from: "

        for x in range(len(quarterx)):
            final = final + "[" + quarterx[x] + "] "
        
        final= final + "\n\n"
    
    #ZERO TIMES
    if len(zerox) > 0:

        final= final + "Takes 0x from: "

        for x in range(len(zerox)):
            final = final + "[" + zerox[x] + "] "
        
        final= final + "\n\n"


    #print(final)
    typeText.configure(text= final)
    if len(calcArray) == 0:
       typeText.configure(text= "No Types Selected") 
                
                    


for x in range(len(dict['typeName'])):
    dict['buttons'].append(Button(dict['typeName'][x], dict['typeChart'][x], dict['typeColor'][x], x))
    
    #print(x)
    

def clear():
    #print("clear was pressed")
    for x in range(len(dict['typeName'])):
            if dict['typeChart'][x] in calcArray:
                 calcArray.remove(dict['buttons'][x].weakness)
                 dict['buttons'][x].button.configure(bg = dict['buttons'][x].button.cget('fg'), fg= '#000000' , relief= 'raised', command= dict['buttons'][x].click)

            dict['buttons'][x].button.configure(state = 'normal')
                 
    typeText.configure(text= "No Types Selected") 

    #print(calcArray)


clearButton = tk.Button(text='Clear', bg= 'Gray', command= clear, height=2, width= 8, font=fontOG, activebackground='#1e1e1e')
clearButton.grid(row= 5, column=0, padx= 10, pady=10)


labelFont = tk.font.Font(family="Small Fonts", size=25)
typeText = tk.Label(app, text='No Types Selected', height=10, width= 45,font=labelFont,fg='#ffffff', bg="#2d2d30", anchor = "center", wraplength = 1000, border=40)
typeText.grid(row= 5, column=1, columnspan=5, rowspan=100,padx=10,pady=10)

signature= tk.Label(app, text='Made by: \n @Duskdragon2000', height=2, width= 15,fg='#919191', bg="#1e1e1e", anchor = "center" )
signature.grid(row= 101, column=0, padx= 10, pady=10)

#print(dict)



app.mainloop()