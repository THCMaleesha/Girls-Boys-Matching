from tkinter import *                                                                                                   #import tkinter module for create the GUIs
from tkinter import messagebox
from functools import partial                                                                                           #import partial for pass arguments to command in tkinter button


main = Tk()
main.geometry("600x500")                                                                           
main.title("WHO IS THE BEST GIRL FOR YOU ")

def choose(boy,girl_1,girl_2,girl_3):
    girl_1 = main.getvar(name=str(girl_1))
    girl_2 = main.getvar(name=str(girl_2))
    girl_3 = main.getvar(name=str(girl_3))
    boy = main.getvar(name=str(boy))

    boy = list(boy)
    boy = list(dict.fromkeys(boy))

    girls = []
    girls.append(girl_1)
    girls.append(girl_2)
    girls.append(girl_3)

    girl_1 = 0
    girl_2 = 0
    girl_3 = 0

    for letter in boy:
        x = girls[0].count(letter)
        girl_1 += x
        y = girls[1].count(letter)
        girl_2 += y
        z = girls[2].count(letter)
        girl_3 += z

    if girl_1 > girl_2:
        name = girls[0]
    elif girl_2 > girl_3:
        name = girls[1]
    else:
        name = girls[2]

    Label(main,text=name,font=14,bg = "pink",width = 20).place(x=320,y=330)
    
    

Label(main,text = "WHO IS THE BEST GIRL FOR YOU",font = ("Helvetica",15)).place(x=150,y=40)

Label(main,text = "Enter your name ",width = 29,font=14,bg = "pink").place(x=50,y=100)
boy = StringVar()
Entry(main,width = 30,textvariable = boy).place(x=320,y=100)
Label(main,text = "Enter 3 girls names that you most like ",font=14,bg = "pink").place(x=50,y=140)
girl_1 = StringVar()
Entry(main,width = 30,textvariable = girl_1).place(x=320,y=140)
girl_2 = StringVar()
Entry(main,width = 30,textvariable = girl_2).place(x=320,y=170)
girl_3 = StringVar()
Entry(main,width = 30,textvariable = girl_3).place(x=320,y=200)

Button(main,text = "CHOOSE",width = 25,height = 2,bg = "pink",command = partial(choose,boy,girl_1,girl_2,girl_3)).place(x=320,y=250)

Label(main,text = "The women that suits you best is ",font=14,bg = "pink").place(x=50,y=330)



main.mainloop()





