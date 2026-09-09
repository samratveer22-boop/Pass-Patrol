import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0
def guess():
    global attempts 
    attempts += 1

    g=int(entry.get())

    if g<number:
        result.config(text="Too Low!")
    elif g<number:
            result.config(text="Too High!")
    elif g<number:
            result.config(text="Correct!")

            count.config(text="Attempts: "+ str(attempts))

def new_game():
      global number, attempts
      number = random.randint(1,100)
      attempts=0
      result.config(text="Guess a number!")
      count.config(text="Attempts: 0")
      entry.delete(0, tk.END)

window=tk.Tk()
window.title("Number Guessing Game")
window.geometry("350x250")
title=tk.Label(window, text="Number Guessing Game", font=("Arial", 18))
title.pack(pady=15)
label=tk.Label(window, text="Guess a number between 1 and 100")
label.pack()

entry=tk.Entry(window)
entry.pack(pady=10)
button=tk.Button(window, text="Guess", command=guess)
button.pack()
result=tk.Label(window, text="Guess a number!")
result.pack(pady=10)

count=tk.Label(window,text="Attempts:0")
count.pack

new = tk.Button(window,text="New Game", command=new_game)
new.pack(pady=10)
window.mainloop()