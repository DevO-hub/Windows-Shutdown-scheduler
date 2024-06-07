import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

def shutdown_at_specific_time(hour, minute, am_pm):
    # Get current time
    current_time = datetime.now()

    # Convert input time to 24-hour format
    if am_pm.upper() == 'PM' and hour != 12:
        hour += 12
    elif am_pm.upper() == 'AM' and hour == 12:
        hour = 0

    # Calculate the target shutdown time
    shutdown_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # If the shutdown time is in the past for today, schedule it for the next day
    if shutdown_time < current_time:
        shutdown_time += timedelta(days=1)

    # Calculate time difference until shutdown
    time_difference = shutdown_time - current_time
    time_seconds = int(time_difference.total_seconds())

    # Execute the shutdown command with the calculated time difference
    os.system(f"shutdown /s /t {time_seconds}")

    # Display confirmation message
    messagebox.showinfo("Scheduled", f"Your PC is scheduled to shutdown at {shutdown_time.strftime('%I:%M %p')}")

def schedule_shutdown():
    try:
        time_part = entry_time.get()
        am_pm = entry_am_pm.get().strip().upper()
        
        # Validate AM/PM input
        if am_pm not in ['AM', 'PM']:
            raise ValueError("Invalid AM/PM format")
        
        hour, minute = map(int, time_part.split(':'))
        
        # Call the shutdown function
        shutdown_at_specific_time(hour, minute, am_pm)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Schedule Shutdown")

# Create and place the input fields and button
tk.Label(root, text="Enter Time (HH:MM)").grid(row=0, column=0, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="AM/PM").grid(row=1, column=0, padx=10, pady=10)
entry_am_pm = tk.Entry(root)
entry_am_pm.grid(row=1, column=1, padx=10, pady=10)

button_schedule = tk.Button(root, text="Schedule Shutdown", command=schedule_shutdown)
button_schedule.grid(row=2, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()
