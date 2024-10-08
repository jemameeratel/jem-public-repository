import tkinter as tk
from tkinter import Label
import requests
from datetime import datetime

# Function to fetch the current time from World Time API
def fetch_online_time():
    try:
        response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Manila')
        data = response.json()
        current_time = data['datetime']
        
        # Correctly parse the datetime with timezone info using strptime and manual format
        formatted_time = datetime.strptime(current_time[:-6], '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
        
        # Update the label with the fetched time
        time_label.config(text=formatted_time)
    except Exception as e:
        # Show error message if something goes wrong
        time_label.config(text="Error retrieving time")
        print(f"Error: {e}")
    
    # Update the time every 10 seconds
    root.after(10000, fetch_online_time)

# Set up the Tkinter window
root = tk.Tk()
root.title("Philippine Time Display (Online)")
root.geometry("600x200")  # Adjust size of the window

# Create a label to display the time
time_label = Label(root, font=('calibri', 45, 'bold'), foreground='black')
time_label.pack(anchor='center', pady=30)  # Add some padding

# Call the function to start fetching the time
fetch_online_time()

# Run the Tkinter main loop to keep the window open
root.mainloop()
