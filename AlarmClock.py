from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print("The set Date is: ",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock App")
clock.geometry("400x200")
time_format = Label(clock, text="Enter Time in 24 Hour Format!!", fg="brown", bg="pink", font="Arial").place(x=60,y=12)
addTime = Label(clock,text="HH : MM : SS",font=60).place(x=120,y=70)
setYourAlarm = Label(clock,text="Set the time:",fg="brown",relief="solid",font=("Helevetica",7,"bold")).place(x=20,y=99)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock,textvariable = hour,bg = "yellow",width = 20).place(x=110,y=100)
minTime = Entry(clock,textvariable = min,bg = "yellow",width = 20).place(x=150,y=100)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 20).place(x=200,y=100)

submit = Button(clock,text = "Set Alarm",fg="white",bg="blue",width = 10,command = actual_time).place(x=110,y=150)

clock.mainloop()