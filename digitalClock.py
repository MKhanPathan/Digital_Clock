from tkinter import Tk, Label

Window = Tk()
Window.title("Digital Clock")
Window.geometry("600x300")
Window.configure(bg="lightblue")
label = Label(Window, font=("Arial Black",78,"bold"), bg="lightblue", fg="black")
label.pack(pady=100)

Window.mainloop()