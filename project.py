# import the modules 
import tkinter
import random

# list of possible colours
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30

# function to start the game
def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    nextColour()

# function to choose and display the next colour
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # check if entered colour == actual colour
        if e.get().lower() == label.cget("fg").lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # update label text & colour
        label.config(fg = colours[1], text = colours[0])

        # update score
        scoreLabel.config(text = "Score: " + str(score))

# countdown timer function 
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# driver code
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text = "Type in the COLOUR of the word, not the word itself!",
                             font = ('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press Enter to start",
                           font = ('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft),
                          font = ('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
