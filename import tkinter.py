import tkinter 

from tkinter import * 

window = Tk()

window.title('Rechner')

expression = ''

window.iconbitmap(r'C:/Users/meezo/Desktop/Unbenannt.ico')



#window.geometry('400x400')



def add(value):
    global expression
    expression += str(value)
    

    label = Label(window, text=expression)
    label.config()
    label.grid(row=0, column=1)

def clear():
    global expression
    expression = ''
    if expression != '':
        expression=''
    label = Label(window, text=expression)
    label.config()
    label.grid(row=0, column=1)
    

def calc():
    global solve
    solve = (eval(expression))
    label = Label(window, text=solve)
    label.config()
    label.grid(row=0, column=4)



#e = Entry(window, textvariable= expression)
#e.grid(row=0, column=0)

button_9 = Button(window, text='9', padx=45, pady=45, command=lambda: add(9))
button_8 = Button(window, text='8', padx=45, pady=45, command=lambda: add(8))
button_7 = Button(window, text='7', padx=45, pady=45, command=lambda: add(7))
button_6 = Button(window, text='6', padx=45, pady=45, command=lambda: add(6))
button_5 = Button(window, text='5', padx=45, pady=45, command=lambda: add(5))
button_4 = Button(window, text='4', padx=45, pady=45, command=lambda: add(4))
button_3 = Button(window, text='3', padx=45, pady=45, command=lambda: add(3))
button_2 = Button(window, text='2', padx=45, pady=45, command=lambda: add(2))
button_1 = Button(window, text='1', padx=45, pady=45, command=lambda: add(1))
button_0 = Button(window, text='0', padx=45, pady=45, command=lambda: add(0))

button_add = Button(window, text='+', padx=45, pady=45, command=lambda: add('+'))
button_sub = Button(window, text='-', padx=45, pady=45, command=lambda: add('-'))
button_mul = Button(window, text='*', padx=45, pady=45, command=lambda: add('*'))
button_div = Button(window, text='/', padx=45, pady=45, command=lambda: add('/'))

button_dot = Button(window, text='.', padx=45, pady=45, command=lambda: add('.'))
button_clear = Button(window, text='C', padx=45, pady=45, command=lambda: clear())
button_equals = Button(window, text='=', padx=205, pady=45, command=lambda: calc())

button_9.grid(row=1, column=3)
button_8.grid(row=1, column=2)
button_7.grid(row=1, column=1)
button_6.grid(row=2, column=3)
button_5.grid(row=2, column=2)
button_4.grid(row=2, column=1)
button_3.grid(row=3, column=3)
button_2.grid(row=3, column=2)
button_1.grid(row=3, column=1)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)

button_dot.grid(row=4, column=3)
button_clear.grid(row=4, column=2)
button_equals.grid(row=5, column=1, columnspan=4)









window.mainloop()