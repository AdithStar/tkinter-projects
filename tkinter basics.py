import tkinter
screen = tkinter.Tk()
screen.geometry("400x400")
screen.title("Tk Basics")
label = tkinter.Label(screen,text = "Enter your equation here",bg = "black", fg = "red", padx = 50,pady = 50 )
entry = tkinter.Entry(screen)
def function():
    button.config(bg = "red", fg = "black")
button = tkinter.Button(screen,text = "=", command = function)
label.pack()
entry.pack()
button.pack()
screen.mainloop()
