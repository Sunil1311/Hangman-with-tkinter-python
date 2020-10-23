#to randomly select a word
import random as rd
#to implement GUI
import tkinter as tk

#create main window 
main_window = tk.Tk()
#window size
main_window.geometry("250x250")
icon = tk.PhotoImage(file="hangman_icon.png")
main_window.iconphoto(False,icon)
main_window.title("Hangman!")
main_frame = tk.Frame(main_window)
canvas = tk.Canvas(main_frame,height=100,width=100)
canvas.grid(row=1)

#global variable declaration 
maxAttempts = 4
attemptsCount = 0
word = ""
secret = ""
hidden = []
game_started = False

#tkinter variables
attempt_var = tk.StringVar()
info_var = tk.StringVar()
word_var = tk.StringVar()
guess_btn_var =tk.StringVar()

#string variables
attempt_text = "You have "+str(maxAttempts-attemptsCount)+" attempts remaining..."
info_text = "Enter a character and press Guess to check!"
enter_word_text = "Enter a character: "
welcome_text = "Welcome to Hangman!"
start_text = "Start!"
guess_text = "Guess!"
play_again_text = "Play Again!"
you_lost_text = "Game over! You lost! Play again?"
victory_text = "You got it! You Won! Play again?"
exit_text = "Exit!"
blank_text = ""

#tkinter variable initialization
attempt_var.set(blank_text)
info_var.set(info_text)
guess_btn_var.set(guess_text)

#frames to add multiple elements in same grid
frame_one = tk.Frame(main_frame)
frame_two = tk.Frame(main_frame)

#labels to show information in window
attempt_label = tk.Label(main_frame,textvariable=attempt_var).grid(row=0)
#matrix_label = tk.Label(main_frame,textvariable=matrix_text_var).grid(row=1)
info_label = tk.Label(main_frame,textvariable=info_var).grid(row=3)
enter_word_label = tk.Label(frame_one,text=enter_word_text)

#text box 
enter_word_entry = tk.Entry(frame_one,width=5)

#packing frames and button in grids
frame_one.grid(row=4)
exit_btn = tk.Button(frame_two,text=exit_text,height=1,width=12,command=main_frame.quit)
frame_two.grid(row=5)
exit_btn.pack(side='left')

# method to get random word
def get_word():
    random_no = rd.randrange(44)
    with open('words.txt') as f:
        lines= f.readlines()
        word= lines[random_no]
    return word


# method checks if game is started or not.
#(called when button "play again" or "guess" button is pressed)
def check():
    if not game_started:
        play()
    else:
        guess()

#method conatains:
#first time intialization of some labels in window 
#variables intialization
def play():
    #use of global variables
    global game_started
    global attemptsCount
    global hidden
    global attempt_text
    global word
    global secret
    #clear text box on mthod call
    enter_word_entry.delete(0,"end")
    #variables intialization
    game_started = True
    guess = ""
    attempt_text = "You have "+str(maxAttempts-attemptsCount)+" attempts remaining..."
    hidden = []
    attemptsCount = 0
    #label text change
    attempt_var.set(attempt_text)
    #get a random word
    word = get_word()
    secret = word[:-1]
    #create a hidden word of same size
    for char in word:
        hidden.append('_')
    #remove last element in line(carriage return)
    hidden.pop()
    #display text box
    enter_word_label.pack(side='left')
    enter_word_entry.pack(side='left')
    #display hidden string
    hiddenString = ' '.join(hidden)
    word_text = "Word : "+hiddenString
    word_var.set(word_text)
    #display hangman matrix
    draw_hangman(0)
    #shows basic information
    info_var.set(info_text)
    guess_btn_var.set(guess_text)
    #shows hidden word in window
    word_label = tk.Label(main_frame,textvariable=word_var).grid(row=2)

#updates hangman matrix when called based on attempts 
def draw_hangman(attempts):
    global canvas
    if(attempts==0):
        #clear cnavas
        canvas.delete("all")
        #stand
        canvas.create_line(10,90,90,90,fill="black")
        canvas.create_line(25,90,25,10,fill="black")
        canvas.create_line(25,15,80,15,fill="black")
        canvas.create_line(25,35,45,15,fill="black")
        #rope
        canvas.create_line(70,15,70,30,fill="black")
    if(attempts==1):
        #clear cnavas
        canvas.delete("all")
        #stand
        canvas.create_line(10,90,90,90,fill="black")
        canvas.create_line(25,90,25,10,fill="black")
        canvas.create_line(25,15,80,15,fill="black")
        canvas.create_line(25,35,45,15,fill="black")
        #rope
        canvas.create_line(70,15,70,30,fill="black")
        #face
        canvas.create_oval(65,30,75,40,outline="black")
    if(attempts==2):
        #clear cnavas
        canvas.delete("all")
        #stand
        canvas.create_line(10,90,90,90,fill="black")
        canvas.create_line(25,90,25,10,fill="black")
        canvas.create_line(25,15,80,15,fill="black")
        canvas.create_line(25,35,45,15,fill="black")
        #rope
        canvas.create_line(70,15,70,30,fill="black")
        #face
        canvas.create_oval(65,30,75,40,outline="black")
        #neck
        canvas.create_line(70,40,70,43,fill="black")
        #stomach
        canvas.create_oval(64,42,76,60,outline="black")
    if(attempts==3):
        #clear cnavas
        canvas.delete("all")
        #stand
        canvas.create_line(10,90,90,90,fill="black")
        canvas.create_line(25,90,25,10,fill="black")
        canvas.create_line(25,15,80,15,fill="black")
        canvas.create_line(25,35,45,15,fill="black")
        #rope
        canvas.create_line(70,15,70,30,fill="black")
        #face
        canvas.create_oval(65,30,75,40,outline="black")
        #neck
        canvas.create_line(70,40,70,43,fill="black")
        #stomach
        canvas.create_oval(64,42,76,60,outline="black")
        #hands
        canvas.create_line(66,44,60,60,fill="black")
        canvas.create_line(74,44,80,60,fill="black")
    if(attempts==4):
        #clear cnavas
        canvas.delete("all")
        #stand
        canvas.create_line(10,90,90,90,fill="black")
        canvas.create_line(25,90,25,10,fill="black")
        canvas.create_line(25,15,80,15,fill="black")
        canvas.create_line(25,35,45,15,fill="black")
        #rope
        canvas.create_line(70,15,70,30,fill="black")
        #face
        canvas.create_oval(65,30,75,40,outline="black")
        #neck
        canvas.create_line(70,40,70,43,fill="black")
        #stomach
        canvas.create_oval(64,42,76,60,outline="black")
        #hands
        canvas.create_line(66,44,60,60,fill="black")
        canvas.create_line(74,44,80,60,fill="black")
        #legs
        canvas.create_line(66,60,65,75,fill="black")
        canvas.create_line(74,60,75,75,fill="black")

#initilizes variables to play again when player wins
def victory():
    global attemptsCount
    global game_started
    attemptsCount = 0
    info_var.set(victory_text)
    game_started = False
    draw_hangman(attemptsCount)
    guess_btn_var.set(play_again_text)

#method called when guess button is pressed
def guess():
    #use of global variables
    global attemptsCount
    global game_started
    global attempt_text
    global word
    global hidden
    #create list of word as strings are immutable
    word_list = list(word)
    #shows updated attempt count on window
    attempt_text = "You have "+str(maxAttempts-attemptsCount)+" attempts remaining..."
    attempt_var.set(attempt_text)
    #updates hangaman matrix
    draw_hangman(attemptsCount)
    
    #get text box text in variable and clear text in text box
    entered_str= str(enter_word_entry.get())
    enter_word_entry.delete(0,"end")
    #if text box is blank show info
    if(len(entered_str)==0):
        info_var.set("Please Enter any character.")
    #if text box contains more than one character
    if(len(entered_str)>1):
        info_var.set("Enter ONE Character only!")
        #panelty!
        attemptsCount+=1
        #update ateempt count and hangman matrix
        attempt_text = "You have "+str(maxAttempts-attemptsCount)+" attempts remaining..."
        attempt_var.set(attempt_text)
        draw_hangman(attemptsCount)
    #if text box contains one char exact
    else:
        #if guess is correct
        if entered_str in word:
            #loop to every alphabet of word
            for i in range(len(word)):
                #store it in temp variable
                char = word[i]
                #if temp matches in word
                if char == entered_str:
                    #update hidden string and word using word list(string immutable)
                    hidden[i] = word[i]
                    word_list[i] = '_'
                    word = ''.join(word_list)
                    #show updated word in window
                    hiddenString = ' '.join(hidden)
                    word_text = "Word : "+hiddenString
                    info_var.set("Yeah! '"+entered_str+"' is the correct guess!")
                    word_var.set(word_text)
                    #if there are no blanks in the hidden word player wins
                    if '_' not in hidden:
                        #call victory
                        victory()
        #if guess is incorrect           
        else:
            #panelty!
            attemptsCount+=1
            #update information on window
            attempt_text = "You have "+str(maxAttempts-attemptsCount)+" attempts remaining..."
            attempt_var.set(attempt_text)
            info_var.set("Wrong! '"+entered_str+"' is not in the word!")
            #update hangman matrix
            draw_hangman(attemptsCount)
            #max attempts reached
            if(attemptsCount>=4):
                game_started = False
                draw_hangman(attemptsCount)
                attemptsCount=0
                guess_btn_var.set(play_again_text)
                info_var.set(you_lost_text)
                word_text = "Word : "+secret
                word_var.set(word_text)

#program entry (main)
if __name__ == "__main__":
    #show welcome text on first time starting the game 
    guess_btn_var.set(start_text)
    info_var.set(welcome_text)
    guess_playAgain_btn = tk.Button(frame_two,textvariable=guess_btn_var,height=1,width=12,command=check)
    guess_playAgain_btn.pack(side='left')
    draw_hangman(4)

#lets main window loop until closed
main_frame.pack()
main_window.mainloop()