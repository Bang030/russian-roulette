import tkinter as tk
from tkinter import messagebox
import random
import time

class RussianRouletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Roulette")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Load the background image
        self.bg_photo = tk.PhotoImage(file="background.png")

        # Resize the background image manually to fit the window (400x300)
        self.bg_photo = self.bg_photo.subsample(2, 2)  # You can adjust this ratio if the image is too large

        # Background label for the image
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Game data
        self.bullets_left = 6
        self.bullet_position = random.randint(0, 5)
        self.current_position = 0

        # Labels and Buttons (placed over the background)
        self.message_label = tk.Label(root, text="Welcome to Russian Roulette!", font=("Helvetica", 16), fg="white", bg="black")
        self.message_label.pack(pady=10)

        self.bullets_label = tk.Label(root, text=f"Bullets left: {self.bullets_left}", font=("Helvetica", 12), fg="white", bg="black")
        self.bullets_label.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="black")
        self.result_label.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), bg="green", fg="white", command=self.start_round)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", font=("Helvetica", 14), bg="red", fg="white", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_round(self):
        if self.bullets_left <= 0:
            messagebox.showinfo("Game Over", "No bullets left! Resetting game.")
            self.reset_game()
            return

        # Simulate the shot
        self.result_label.config(text="Spinning and firing...")
        self.root.after(1000, self.process_shot)

    def process_shot(self):
        if self.current_position == self.bullet_position:
            self.result_label.config(text="Bang! You died.")
            self.start_button.config(state=tk.DISABLED)
            messagebox.showinfo("Game Over", "You lost the game! Restarting...")
            self.reset_game()
        else:
            self.result_label.config(text="Click! You're safe.")
            self.bullets_left -= 1
            self.bullets_label.config(text=f"Bullets left: {self.bullets_left}")
            self.current_position = (self.current_position + 1) % 6

    def reset_game(self):
        # Reset the game
        self.bullets_left = 6
        self.bullet_position = random.randint(0, 5)
        self.current_position = 0
        self.result_label.config(text="")
        self.bullets_label.config(text=f"Bullets left: {self.bullets_left}")
        self.start_button.config(state=tk.NORMAL)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RussianRouletteApp(root)
    root.mainloop()
