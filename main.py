#Time Counter
import time
from tkinter import *
import tkinter.messagebox

#Set up
root = Tk()
root.geometry("300x300")
root.title("Time Counter")

#To get initial number display in time boxes and identify all as string variables
hour = StringVar()
hour.set("00")

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

#Hours - entry
hour_box = Entry(root, font = ("Times New Roman", 20, "bold"), textvariable = hour, width = 3)
hour_box.place(x = 100, y = 50)

#Minutes - Entry
minute_box = Entry(root, font = ("Times New Roman", 20, "bold"), textvariable = minute, width = 3)
minute_box.place(x = 150, y = 50)

#Seconds - Entry
second_box = Entry(root, font = ("Times New Roman", 20, "bold"), textvariable = second, width = 3)
second_box.place(x = 200, y = 50)

#Timer - Function
def timer():
    try:
        temp = (int(hour.get())*3600) + (int(minute.get())*60) + (int(second.get()))
    except:
        print("Please enter correct numerical values...")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0

        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            tkinter.messagebox.showinfo("Done", "Time is up")

        temp -= 1
    
#Set Time Countdown
set_time_countdown = Button(root, text = "Set Timer Countdown", command = timer)
set_time_countdown.place(x = 100, y = 150)

root.mainloop()