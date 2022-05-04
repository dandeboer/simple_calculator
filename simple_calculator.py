from tkinter import *

root = Tk()
root.title("Simple Calculator")
locked = False

def insert_char(c):
    if locked == False:
        screen['state'] = 'normal'
        current = screen.get()
        screen.delete(0, END)
        screen.insert(0, current + c)
        screen['state'] = 'readonly'
        screen.xview("end")

def clear():
    screen['state'] = 'normal'
    screen.delete(0, END)
    screen['state'] = 'readonly'
    global locked 
    locked = False

def evaluate():
    try:
        e = eval(screen.get())
        screen['state'] = 'normal'
        screen.delete(0, END)
        screen.insert(0, e)
        screen['state'] = 'readonly'
    except:
        screen['state'] = 'normal'
        screen.delete(0, END)
        screen.insert(0, 'MATH ERROR: PRESS CLEAR')
        screen['state'] = 'readonly'
        global locked 
        locked = True
    

screen = Entry(root, width=20,  state='readonly')
screen.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

button1 = Button(root, text='1', command=lambda: insert_char('1'))
button1.grid(row=1, column=0, pady=5)
button2 = Button(root, text='2', command=lambda: insert_char('2'))
button2.grid(row=1, column=1, pady=5)
button3 = Button(root, text='3', command=lambda: insert_char('3'))
button3.grid(row=1, column=2, pady=5)
button4 = Button(root, text='4', command=lambda: insert_char('4'))
button4.grid(row=2, column=0, pady=5)
button5 = Button(root, text='5', command=lambda: insert_char('5'))
button5.grid(row=2, column=1, pady=5)
button6 = Button(root, text='6', command=lambda: insert_char('6'))
button6.grid(row=2, column=2, pady=5)
button7 = Button(root, text='7', command=lambda: insert_char('7'))
button7.grid(row=3, column=0, pady=5)
button8 = Button(root, text='8', command=lambda: insert_char('8'))
button8.grid(row=3, column=1, pady=5)
button9 = Button(root, text='9', command=lambda: insert_char('9'))
button9.grid(row=3, column=2, pady=5)
button0 = Button(root, text='0', command=lambda: insert_char('0'))
button0.grid(row=4, column=0, pady=5)
button_plus = Button(root, text='+', command=lambda: insert_char('+'))
button_plus.grid(row=4, column=1, pady=5)
button_minus = Button(root, text='-', command=lambda: insert_char('-'))
button_minus.grid(row=4, column=2, pady=5)

button_clear = Button(root, text='C', command=clear)
button_clear.grid(row=5, column=0, pady=5)
button_equals = Button(root, text='=', command=evaluate)
button_equals.grid(row=5, column=1, columnspan=2, pady=5)

root.mainloop()