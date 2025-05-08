
import tkinter as tk
from time import strftime
from datetime import datetime

# Initialize Tkinter window
root = tk.Tk()
root.title("Digital Clock")

def time():
    """Update the label with the current time and correct date."""
    current_time = strftime('%H:%M:%S %p')  # Get current time
    current_date = datetime.today().strftime('%d-%m-%Y')  # Get the correct date

    label.config(text=f"{current_time}\n{current_date}")
    label.after(1000, time)  # Refresh every second

# Create Label for displaying the clock
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

# Start updating the time
time()

# Run the Tkinter event loop
root.mainloop()
