import tkinter
import time
screen = tkinter.Tk()
screen.geometry("250x100")
screen.title("Digital Clock")
label = tkinter.Label(screen,text = "",font = ("Arial",30,"bold"))
label.grid(row = 1, column = 1)
def function():
    clock = time.strftime("%I:%M:%S:%p")
    label.config(text = clock)
    label.after(1000,function)
function()
screen.mainloop()