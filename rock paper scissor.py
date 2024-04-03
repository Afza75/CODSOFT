import random
from tkinter import *

m = Tk()
m.title("Rock, Paper, Scissor Game")

# Colors
bg_color = "#f0f0f0"
button_color = "#436850"

l = ['rock', 'paper', 'scissor']
my_score = 0
opponent_score = 0


def play_round(player_choice):
    global my_score, opponent_score

    player1 = player_choice
    player2 = random.choice(l)

    my_choice_label.config(text=f"You Choice: {player1}", fg="#ADBC9F",)
    opponent_choice_label.config(text=f"Opponent's Choice: {player2}", fg="#ADBC9F",)

    if player1 == "rock" and player2 == "paper":
        result_label.config(text="Opponent Won", fg="#ADBC9F",)
        opponent_score += 1

    elif player1 == "scissor" and player2 == "paper":
        result_label.config(text="You Won", fg="#ADBC9F",)
        my_score += 1

    elif player1 == "rock" and player2 == "scissor":
        result_label.config(text="You Won", fg="#ADBC9F",)
        my_score += 1

    elif player1 == "paper" and player2 == "rock":
        result_label.config(text="You Won", fg="#ADBC9F",)
        my_score += 1

    elif player1 == "paper" and player2 == "scissor":
        result_label.config(text="Opponent Won", fg="#ADBC9F")
        opponent_score += 1

    elif player1 == "scissor" and player2 == "rock":
        result_label.config(text="Opponent Won", fg="#ADBC9F")
        opponent_score += 1

    elif player1 == player2:
        result_label.config(text="Match Draw", fg="#ADBC9F")

    disable_buttons()

def conti(a):

    if a == "no":
        disable_buttons()

        final_Label = Label(m, text="Final Score", bg="#ADBC9F", fg="white", font=10)
        final_Label.grid(row=8, column=0, padx=10, pady=10)  # Place final score label

        my = Label(m, text=f"My Score: {my_score}", bg=bg_color, fg="#ADBC9F", font=10, width=20)
        my.grid(row=9, column=0, padx=10, pady=10)  # Place my score label and adjust width

        opponent = Label(m, text=f"Opponent's Score: {opponent_score}", bg=bg_color, fg="#ADBC9F", font=10, width=20)
        opponent.grid(row=9, column=1, padx=10, pady=10)  # Place opponent score label and adjust width

    else:
        enable_buttons()

def disable_buttons():
    rock_button.config(state="disabled", bg=bg_color)
    paper_button.config(state="disabled", bg=bg_color)
    scissors_button.config(state="disabled", bg=bg_color)

def enable_buttons():
    rock_button.config(state="normal", bg=button_color)
    paper_button.config(state="normal", bg=button_color)
    scissors_button.config(state="normal", bg=button_color)

my_choice_label = Label(m, width=25, bg=bg_color,font=10)
my_choice_label.grid(row=1, column=0, padx=10, pady=10)

opponent_choice_label = Label(m, width=25, bg=bg_color,font=10)
opponent_choice_label.grid(row=2, column=0, padx=10, pady=10)

result_label = Label(m, width=20, bg=bg_color,font=10)
result_label.grid(row=3, column=0, padx=10, pady=10)

rock_button = Button(m, text="Rock", command=lambda: play_round("rock"), bg=button_color,width=9, fg="white",font=10)
rock_button.grid(row=3, column=1, padx=10, pady=10)

paper_button = Button(m, text="Paper", command=lambda: play_round("paper"), bg=button_color,width=9, fg="white",font=10)
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = Button(m, text="Scissors", command=lambda: play_round("scissor"),width=9, bg=button_color, fg="white",font=10)
scissors_button.grid(row=2, column=1, padx=10, pady=10)

continue_Label = Label(m, text="Do you want to continue ?", bg="#ADBC9F", fg="white",font=10)
continue_Label.grid(row=6, column=0, padx=10, pady=10)

continue_button_no = Button(m, text="No",width=4, command=lambda: conti("no"), bg=button_color, fg="white",font=10)
continue_button_no.grid(row=6, column=1, padx=10, pady=10)

continue_button_yes = Button(m, text="Yes", width=4,command=lambda: conti("yes"), bg=button_color,font=10,fg="white")
continue_button_yes.grid(row=6, column=2, padx=10, pady=10)

game_title = Label(m, text="Rock Paper Scissor Game", font=("Arial", 18, "bold"),bg="#12373A", fg="white")
game_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

m.mainloop()

