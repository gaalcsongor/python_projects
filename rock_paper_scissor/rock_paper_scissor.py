# main design for the rock, paper, scissors game
import random
import sys
import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self):
        self.player = ""
        self.bet = 0
        self.player_balance = 100
        self.computer_balance = 10

        self.window = tk.Tk()
        self.window.title("rock, paper, scissors game")
        self.window.geometry("600x400")
        
        self.label_main = tk.Label(self.window, text="A simple game of rock, paper, scissors", font=("Arial", 16))
        self.label_main.pack(padx=20, pady=(10, 10))
        
        self.label_bet = tk.Label(self.window, text="How much do you want to bet?", font=("Arial", 12))
        self.label_bet.pack(padx=20, pady=(20, 0))
        
        self.button_frame_1 = tk.Frame(self.window) 
        self.button_frame_1.columnconfigure(0, weight=1) 
        self.button_frame_1.columnconfigure(1, weight=1)
        self.button_frame_1.columnconfigure(2, weight=1)
        
        self.btn_10 = tk.Button(self.button_frame_1, text="10$", font=("Arial", 10), command=self.player_bet_10)
        self.btn_10.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn_20 = tk.Button(self.button_frame_1, text="20$", font=("Arial", 10), command=self.player_bet_20)
        self.btn_20.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.btn_30 = tk.Button(self.button_frame_1, text="30$", font=("Arial", 10), command=self.player_bet_30)
        self.btn_30.grid(row=0, column=2, sticky=tk.W+tk.E)
        
        self.button_frame_1.pack(padx=20, pady=(20, 10), fill="x")    
        
        self.label_choice = tk.Label(self.window, text="What is your choice?", font=("Arial", 12))
        self.label_choice.pack(padx=20, pady=(50, 10))    
        
        self.button_frame_2 = tk.Frame(self.window) 
        self.button_frame_2.columnconfigure(0, weight=1) 
        self.button_frame_2.columnconfigure(1, weight=1)
        self.button_frame_2.columnconfigure(2, weight=1)
        
        self.btn_rock = tk.Button(self.button_frame_2, text="rock", font=("Arial", 10), command=self.player_rock)
        self.btn_rock.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn_paper = tk.Button(self.button_frame_2, text="paper", font=("Arial", 10), command=self.player_paper)
        self.btn_paper.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.btn_scissor = tk.Button(self.button_frame_2, text="scissor", font=("Arial", 10), command=self.player_scissor)
        self.btn_scissor.grid(row=0, column=2, sticky=tk.W+tk.E)
        
        self.button_frame_2.pack(padx=20, pady=(10, 10), fill="x")
        
        self.btn_play = tk.Button(self.window, text="play a game", font=("Arial", 12), command=self.play_game)
        self.btn_play.pack(padx=20, pady=(40, 0))

        self.window.mainloop()
        
    
    def player_rock(self):
        messagebox.showinfo(title=None, message="player's choice is rock")
        self.player = "rock"
    
    
    def player_paper(self):
        messagebox.showinfo(title=None, message="player's choice is paper")
        self.player = "paper"

    
    def player_scissor(self):
        messagebox.showinfo(title=None, message="player's choice is scissor")
        self.player = "scissor"
        
    
    def player_bet_10(self):
        messagebox.showinfo(title=None, message="player bets 10$")
        self.bet = 10
    
    
    def player_bet_20(self):
        messagebox.showinfo(title=None, message="player bets 20$")
        self.bet = 20
        
    
    def player_bet_30(self):
        messagebox.showinfo(title=None, message="player bets 30$")
        self.bet = 30


    def comp_choice(self):
        items = ["rock", "paper", "scissor"]    
        return random.choice(items)
    
    
    def get_result(self, player, comp):
        # 0 - tie, 1 - player wins, 2 - comp wins
        if player == "rock":
            if comp == "rock":
                return "it's a tie"
            elif comp == "paper":
                return "computer wins"
            else:
                return "player wins"
        elif player == "paper":
            if comp == "rock":
                return "player wins"
            elif comp == "paper":
                return "it's a tie"
            else:
                return "computer wins"
        elif player == "scissor":
            if comp == "rock":
                return "computer wins"
            elif comp == "paper":
                return "player wins"
            else:
                return "it's a tie"
            
            
    def calculate_balance(self, result, bid, player_balance, comp_balance):
        if result == "player wins":
            player_balance += bid
            comp_balance -= bid
        elif result == "computer wins":
            player_balance -= bid
            comp_balance += bid
        return player_balance, comp_balance


    def play_game(self):
        if self.bet == 0:
            messagebox.showinfo(title="error message", message="player didn't make a bet!")
        elif self.player == "":
            messagebox.showinfo(title="error message", message="player didn't pick!")
        else:
            self.computer = self.comp_choice()
            self.result = self.get_result(self.player, self.computer)
            self.player_balance, self.computer_balance = self.calculate_balance(
                self.result, self.bet, self.player_balance, self.computer_balance)
            if self.computer_balance <= 0:
                messagebox.showinfo(title=None, message="player has won the game!")
                sys.exit()
            elif self.player_balance <= 0:
                messagebox.showinfo(title=None, message="computer has won the game!")
                sys.exit()
            messagebox.showinfo(
                title=None, message=f"player: {self.player}\n"
                f"computer: {self.computer}\n"
                f"bet: {self.bet}$\n"
                f"result: {self.result}\n"
                f"player account: {self.player_balance}$\n"
                f"computer account: {self.computer_balance}$") 
        

if __name__ == "__main__":
    game = UserInterface()        