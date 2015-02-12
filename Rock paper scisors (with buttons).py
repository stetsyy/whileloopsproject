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
        Choice = simpledialog.askinteger("Choice",
                                "What is your choice?" +\
                                " Choose 1 for rock, " +\
                                " Choose 2 for paper, " +\
                                " choose 3 for scissors")

        class AllTkinterWidgets:
            def __init__(self, master):
                frame = Frame(master, width=500, height=400, bd=1)
                frame.pack()

                iframe1 = Frame(frame, bd=2, relief=SUNKEN)
                Button(iframe1, text='ROCK').pack(side=LEFT, padx=5)

                v=IntVar()
                iframe1.pack(expand=1, fill=X, pady=10, padx=5)
                
                frame = Frame(master, width=500, height=400, bd=1)
                frame.pack()

                iframe1 = Frame(frame, bd=2, relief=SUNKEN)
                Button(iframe1, text='PAPER').pack(side=LEFT, padx=5)

                v=IntVar()
                iframe1.pack(expand=1, fill=X, pady=10, padx=5)

                frame = Frame(master, width=500, height=400, bd=1)
                frame.pack()

                iframe1 = Frame(frame, bd=2, relief=SUNKEN)
                Button(iframe1, text='SCISSORS').pack(side=LEFT, padx=5)

                v=IntVar()
                iframe1.pack(expand=1, fill=X, pady=10, padx=5)
                
        #root.option_add('*font', ('verdana', 10, 'bold'))
        all = AllTkinterWidgets(root)
        root.title('Tkinter Widgets')
        root.mainloop()

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


