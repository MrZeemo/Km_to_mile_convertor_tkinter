from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=500)



my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()
my_label.grid(column=0, row=0)



button = Button(text="Click Me")

button.grid(column=1, row=1)


button_1 = Button(text="Me", command=button_clicked)
button_1.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()