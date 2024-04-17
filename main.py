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
    entry_login = simpledialog.askstring("Note Log", f"{user_time()}\nNote Log(Y/N): ", parent=root) # Prompt user for input using a dialog box
    if entry_login == "y" or entry_login == "yes": # If user input is 'Y' or 'Yes'
        daily_user_note = simpledialog.askstring("Enter Notes", "Enter Notes Here:", parent=root) # Prompt user to enter notes using a dialog box
        if daily_user_note: # If user provided some notes
            return f"{user_time()}\n\n{daily_user_note}" # Return the formatted notes including timestamp
    return None

def note_window():
    def open_note_dialog():
        # Create a new Toplevel window for note input
        note_dialog = tk.Toplevel()
        note_dialog.title("Enter Notes")

        # Create a label for instructions
        tk.Label(note_dialog, text="Enter Notes Here:").pack()

        # Create a text entry widget for the user to input notes
        note_entry = tk.Text(note_dialog, height=10, width=50)
        note_entry.pack()

        # Create a button to submit the notes
        submit_button = tk.Button(note_dialog, text="Submit", command=lambda: save_notes(note_entry.get("1.0", "end-1c"), note_dialog))
        submit_button.pack()

    def save_notes(notes, dialog):
        if notes.strip(): # Check if notes are not empty
            with open("userlogs.txt", "a") as notesFile:
                notesFile.write(f"{user_time()}\n\n{notes}\n") # Append the notes to the log file
            dialog.destroy() # Close the dialog window
            add_log(notes) # Call add_log function with the entered notes

    # Create the main Tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    # Prompt user to enter notes
    open_note_dialog()

    root.mainloop() # Start the Tkinter event loop

# Call the note_window function to start note entry
note_window()
