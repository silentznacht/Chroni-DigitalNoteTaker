import datetime

####################################################################################################
#                                                                  /\_/\                           #
#                                                                 ( o.o )                          #
#                                                                  > ^ <                           #
#                                                          [Author: @silentznacht]                 #
####################################################################################################


with open("userlogs.txt", "a") as notesFile:
    
    def user_time(): # formats time
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("\n" + "-" + "%Y-%m-%d %I:%M %p" + "-")
        return formatted_time

    def user_notes(): # takes in user input, returns it so that it may used in the add_log func
        entry_login = input(user_time() + "\nNote Log(Y/N): ").lower()
        if entry_login == "y" or entry_login == "yes":
            daily_user_note = input("Enter Notes Here: ")
            if daily_user_note:
                return user_time() + "\n\n" + daily_user_note
        return None

    def add_log():
            note = user_notes() # note = return value of user input
            if note:
                with open("userlogs.txt", "a") as notesFile:
                    notesFile.write(note + "\n") # appends to file user note

    add_log() # executes 
