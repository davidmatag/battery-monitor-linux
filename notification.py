import tkinter as tk
import tkinter.font as tkFont


notification = tk.Tk()

notification.configure(background="blue")
notification.title("Battery low")
notification.geometry("355x150")

font_style_title = tkFont.Font(family="Lucida Grande", weight="bold", size=15)

title = tk.Label(
    notification,
    text="Your battery is running low",
    fg="white",
    bg="blue",
    font=font_style_title
).place(x=20, y=25)

text = tk.Label(
    notification,
    text="You might want to plug in your PC",
    fg="white",
    bg="blue"
).place(x=20, y=57)


def dispose_notification():
    notification.destroy()


btn_Close = tk.Button(
    notification,
    text="Close",
    command= dispose_notification
).place(x=267, y=100)


def show_notification():
    notification.mainloop()
