import tkinter as tk
import random

# Game settings
WIDTH = 400
HEIGHT = 400
BOX_SIZE = 50
TIME_LIMIT = 30

score = 0
time_left = TIME_LIMIT
game_running = False

# Create window
root = tk.Tk()
root.title("Tap The Box Game")
root.geometry("450x520")
root.resizable(False, False)

# Labels
title_label = tk.Label(root, text="Tap The Box!", font=("Arial", 18))
title_label.pack()

time_label = tk.Label(root, text=f"Time: {TIME_LIMIT}", font=("Arial", 14))
time_label.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

# Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(pady=10)

# Create box
box = canvas.create_rectangle(0, 0, BOX_SIZE, BOX_SIZE, fill="red")
canvas.itemconfig(box, state="hidden")


def move_box():
    if not game_running:
        return

    x = random.randint(0, WIDTH - BOX_SIZE)
    y = random.randint(0, HEIGHT - BOX_SIZE)
    canvas.coords(box, x, y, x + BOX_SIZE, y + BOX_SIZE)
    root.after(800, move_box)


def box_clicked(event):
    global score
    if game_running:
        score += 1
        score_label.config(text=f"Score: {score}")
        move_box()


def countdown():
    global time_left, game_running

    if time_left > 0 and game_running:
        time_left -= 1
        time_label.config(text=f"Time: {time_left}")
        root.after(1000, countdown)
    else:
        game_running = False
        canvas.itemconfig(box, state="hidden")
        tk.messagebox.showinfo("Game Over", f"Your Score: {score}")


def start_game():
    global score, time_left, game_running

    score = 0
    time_left = TIME_LIMIT
    game_running = True

    score_label.config(text="Score: 0")
    time_label.config(text=f"Time: {TIME_LIMIT}")

    canvas.itemconfig(box, state="normal")
    move_box()
    countdown()


start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=5)

canvas.bind("<Button-1>", box_clicked)

root.mainloop()






