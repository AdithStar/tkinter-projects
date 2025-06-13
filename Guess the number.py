import tkinter
import random
import tkinter.messagebox
screen = tkinter.Tk()
screen.geometry("400x300")
screen.title("Guess the number")
label = tkinter.Label(screen,text = "Guess the number between 1-20")
entry = tkinter.Entry(screen)
 
randomdigit = random.randint(1,20)
def function():
    guess = int(entry.get())
    if guess == randomdigit:
        tkinter.messagebox.showinfo("Guess the number","You guessed it!")
    elif guess > randomdigit:
        tkinter.messagebox.showinfo("Guess the number","A little high") 
    elif guess < randomdigit:
        tkinter.messagebox.showinfo("Guess the number","A little low")
button = tkinter.Button(screen,text = "Guess", command = function)

def function1():
    global randomdigit
    randomdigit = random.randint(1,20)
    
button1 = tkinter.Button(screen,text = "Reset",command = function1 )
label.pack()
entry.pack()
button.pack()
button1.pack()
screen.mainloop()

