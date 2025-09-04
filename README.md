Hi I am Debanjan Guchhait

🌱 I’m currently learning various softskills

💬 I am an ECE graduate from Techno Main Salt Lake


This is a Color Recognition Game built in Python using Tkinter.
The goal is to type the color of the text displayed on the screen, not the text itself. For example, if the word ‘Blue’ is written in red color, the correct answer is ‘Red’. The game runs on a countdown timer, and the score increases each time the player enters the right answer.


1. Modules & Variables

import tkinter
import random

tkinter is used to create the GUI (buttons, labels, input fields).

random is used to shuffle the list of colors.


We keep:

score → to track correct answers

timeleft → to track the countdown timer

colours → a list of color names


2. Game Start

def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    nextColour()

The game starts when the user presses Enter.

If the timer is still at the initial 30 seconds, it begins counting down.

Then it immediately shows the first color challenge with nextColour().



3. Next Colour Logic

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == label.cget("fg").lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = colours[1], text = colours[0])
        scoreLabel.config(text = "Score: " + str(score))


First, it checks if the game is still running (timeleft > 0).

It compares the user input (e.get()) with the actual text color (label.cget("fg")).

If correct → score increases.


The entry field is cleared for the next attempt.

The colours list is shuffled, and:

label text is set to one color name,

The font color is set to a different random color.


Updates the scoreLabel with the current score.


4. Countdown Timer

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

Decreases timeleft by 1 every second.

Uses after(1000, countdown) to recursively call itself every 1 second.

Updates the time label until time runs out.



5. Driver Code (UI Setup)

root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

Creates the main window (root).


Then we add:

Instructions Label → tells the player the rules.

Score Label → initially “Press Enter to start”.

Time Label → shows remaining time.

Main Color Label → large font, displays the word.

Entry Widget → player types the answer here.


Finally:

root.bind('<Return>', startGame)
root.mainloop()

Binds the Enter key to start the game.

mainloop() runs the GUI until the window is closed.

This how the project works.......



