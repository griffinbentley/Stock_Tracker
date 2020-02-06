from tkinter import *

def window():
    window = Tk()


    def printName():
        print('Chello my name is Griffin!')

    button_1 = Button(window, text='Print my name', command=printName)
    button_1.pack()


    window.mainloop()