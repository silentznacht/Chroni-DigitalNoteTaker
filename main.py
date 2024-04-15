import datetime
import datetime
import tkinter as tk
from tkinter import simpledialog

####################################################################################################
#                                                                  /\_/\                           #
#                                                                 ( o.o )                          #
#                                                                  > ^ <                           #
#                                                          [Author: @silentznacht]                 #
####################################################################################################

def user_time(): # formats time
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %I:%M %p")
    return formatted_time

def user_notes(): # takes in user input, returns it so that it may be used in the add_log func
    root = tk.Tk() # Create a Tkinter root window
    root.withdraw()  # Hide the main window to show only the dialog box
    entry_login = simpledialog.askstring("Note Log", f"{user_time()}\nNote Log(Y/N): ").lower() # Prompt user for input using a dialog box
    if entry_login == "y" or entry_login == "yes": # If user input is 'Y' or 'Yes'
        daily_user_note = simpledialog.askstring("Enter Notes", "Enter Notes Here:") # Prompt user to enter notes using a dialog box
        if daily_user_note: # If user provided some notes
            return f"{user_time()}\n\n{daily_user_note}" # Return the formatted notes including timestamp
    return None

def add_log():
    note = user_notes() # Get user input notes
    if note: # If user provided notes
        with open("userlogs.txt", "a") as notesFile:
            notesFile.write(note + "\n") # Append the notes to the log file

add_log() # Execute the function to add notes to the log file
