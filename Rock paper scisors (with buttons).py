from tkinter import *
root = Tk()
master = Tk()
def main():
    import tkinter.simpledialog as simpledialog
    import tkinter.messagebox as messagebox
    from random import randint
    cpuwins = 0
    wins = 0
    messagebox.showinfo("HEY","Lets play rock paper scissors. Best 2 outta 3.")

   
    while wins < 2 and cpuwins < 2:
        b1['command']=b1Click
        b2['command']=b2Click
        b3['command']=b3Click

        b1 = Button(None, text="ROCK", command="rock")
        b1.pack()

        b2 = Button(None, text="PAPER", command="paper")
        b2.pack()

        b3 = Button(None, text="SCISSORS", command="scissors")
        b3.pack()
    

        if Choice == "rock":
            Choice = 1
        elif Choice == "paper":
            Choice = 2
        elif Choice == "scissors":
            Choice = 3
            
        CpuChoice = randint(1,3) 
        if Choice == CpuChoice:
            messagebox.showinfo("TIE","We had the same")
        elif Choice == 1 and CpuChoice== 3:
            messagebox.showinfo ("YOU WIN!","Rock smashes scissors")
            wins += 1
        elif Choice == 3 and CpuChoice== 1:
            messagebox.showinfo("I WIN!","Rock smashes scissors")
            cpuwins += 1
        elif Choice == 1 and CpuChoice== 2:
            messagebox.showinfo("I WIN!","Paper covers rock")
            cpuwins += 1
        elif Choice == 2 and CpuChoice== 1:
            messagebox.showinfo("YOU WIN!","paper covers rock" )
            wins += 1
        elif Choice == 2 and CpuChoice== 3:
            messagebox.showinfo("I WIN!","Scissors cuts paper")
            cpuwins += 1
        elif Choice == 3 and CpuChoice== 2:
            messagebox.showinfo("YOU WIN!","Scissors cuts paper")
            wins += 1
        elif Choice == 1 and CpuChoice== 2:
            messagebox.showinfo("I WIN!","You lose")
            cpuwins += 1
        else:
            messagebox.showinfo ("Error","Oops try again")
            
main()
Choice = 0
while Choice != "no":
    Choice = simpledialog.askstring("Choice",
                                "Would you like to play again?")
    if Choice == "yes":
        main()
    elif Choice == "no":
        root.destroy()


