# modules and global variabels
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


alarm_time = None
window = tk.Tk()
window.title('Clock')
window.resizable(width=False, height=False)
window.geometry('500x400')




# function for getting current time

def get_current_time():
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    compare_alarm_with_current_time(current_time)
    window.after(1000,get_current_time)



# function set allarm time 
def set_alarm():
    global alarm_time
    current_time = datetime.now()
    alarm_time = current_time.replace(hour=int(hour_entry.get()),minute=int(minut_entry.get()),second=0,microsecond=0)
    latest_alarm_label .configure(text=alarm_time.strftime("%H:%M:%S"))





# function for comparing time with alarm
def compare_alarm_with_current_time(current_time):
    global alarm_time
    if alarm_time is not None and current_time >= alarm_time:
        messagebox.showinfo("showinfo", "Your alarm has happened")
        latest_alarm_label.configure(text='No alarm has been set')
        alarm_time = None





# ui design
# text time
time_label = tk.Label(window,text = '10:30:30',font=("Tahoma", 32))
time_label.pack()


# text input hour
# input entry

tk.Label(window,text="Hour").pack()
hour_entry = tk.Entry(window)
hour_entry.pack()



# text input minut
# input entry

tk.Label(window,text="Minut").pack()
minut_entry = tk.Entry(window)
minut_entry.pack()



# buttom set allarm
tk.Button(window, text="set alarm", command=set_alarm).pack()

# showing last alarm

latest_alarm_label = tk.Label(window, text='No alarm has been set')
latest_alarm_label.pack()




# running application
get_current_time()
window.mainloop()