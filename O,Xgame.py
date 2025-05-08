
import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check all winning conditions and highlight the winner."""
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")

            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    """Handles button clicks and toggles between 'X' and 'O'."""
    global current_player
    
    if buttons[index]["text"] == "":  # Only allow empty buttons to be clicked
        buttons[index]["text"] = current_player
        check_winner()
        
        # Switch players
        current_player = "X" if current_player == "O" else "O"
        label.config(text=f"Player {current_player}'s turn")

# Initialize Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize player
current_player = "X"

# Display player turn label
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the game loop
root.mainloop()
