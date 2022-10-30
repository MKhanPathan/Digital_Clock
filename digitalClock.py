from tkinter import Tk, Label
from datetime import datetime

Window = Tk()
Window.title("Digital Clock")
Window.geometry("600x300")
Window.configure(bg="lightblue")
label = Label(Window, font=("Arial Black",78,"bold"), bg="lightblue", fg="black")
label.pack(pady=100)

def clock():
    time=datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
Window.mainloop()