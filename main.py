from tkinter import *

def calculate():
    miles = float(input.get())
    km = miles * 1.6
    answer.config(text=f"{km}")
window= Tk()
window.minsize(width=500,height=500)
window.title("Mile to Km converter")


is_equal_to = Label(text="is equal to", font=("Ariel", 24))
is_equal_to.grid(column=0,row=1)

input = Entry()
input.grid(column=1, row=0)


miles = Label(text="Miles", font=("Ariel", 24))
miles.grid(column=2, row=0)

answer = Label(text="0", font=("Ariel", 24))
answer.grid(column=1, row=1)

calculate = Button(text="Calculate", command= calculate)
calculate.grid(column=1, row=2)

km = Label(text="Km", font=("Ariel", 24))
km.grid(column=2, row=1)













window.mainloop()