from tkinter import * 
from tkinter import messagebox
import json
import requests
import webbrowser
import asyncio

root = Tk()
root.attributes('-topmost', True)
root.geometry('400x400')
root.resizable(False, False)
main_menu = Menu(root)
menubar = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Info", menu=menubar)

def github():
    webbrowser.open('https://github.com/Mineplay3/SpamHook')

menubar.add_command(label="Github Source", command=github)
menubar.add_separator()
menubar.add_command(label="Made by: Mineplay3")

root.config(menu=main_menu)

async def send():
    usernam = username.get()
    
    if usernam == "":
        usernam = "https://github.com/Mineplay3/SpamHook"

    url = webhook.get()
    
    if url == "":
        messagebox.showerror(title="Invalid Webhook Url", message="You need to specify a webhook")
        return

    if "https://discord.com/api/" not in url:
        messagebox.showerror(title="Invalid Webhook Url", message="Invalid Webhook url")
        return

    json = {
        'username': usernam,
        'content': message.get()
    }
    a = 0


    while a <= amount.get():
        pog = requests.post("https://discord.com/api/v8/webhooks/819653001236971541/L9tsN3qft4sbb1NuVEoLFGMpsfDohpBstf03n31ohJGr-yJ_K7a2vQ2jYoQyBMQLHDMI?wait=false", json=json)
        a +=1
        root.update()
        
        return

        
def starter():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send())

root.title("SpamHook")
root.configure(background="#36393f")
webhook = Entry(root)
webhook.grid(row=1, column=2, columnspan=1)

text1 = Label(root, text="Webhook Url")
text1.grid(row=1, column=1)

message = Entry(root)
message.grid(row=2, column=2, columnspan=1)

text2 = Label(root, text="Message")
text2.grid(row=2, column=1)

username = Entry(root)
username.grid(row=3, column=2, columnspan=1)

text3 = Label(root, text="Webhook Name")
text3.grid(row=3, column=1)

amount = Scale(root, from_=1, to=300, orient=HORIZONTAL, background="#36393f", showvalue=0)
amount.grid(row=4, column=2, columnspan=1)

amount.set(1)

def textup4():
    text4 = Label(root, text=f"Spam Quantity ({amount.get()})")
    text4.grid(row=4, column=1)
    root.update()
    root.after(10, textup4) 

textup4()

delay = Scale(root, from_=10, to=3000, orient=HORIZONTAL, background="#36393f", showvalue=0)
delay.grid(row=5, column=2, columnspan=1)
delay.set(10)

def textup5():
    text5 = Label(root, text=f"Spam Delay ({delay.get()} ms)")
    text5.grid(row=5, column=1)
    root.update()
    root.after(10, textup5) 

textup5()

start = Button(root, text="Spam", command=starter, borderwidth=0, background="#36393f")
start.grid(row=6, column=2, columnspan=1)
img1 = PhotoImage(file="Images/spam.png")
start.config(image=img1)

close = Button(root, text="Close", command=root.destroy, borderwidth=0, background="#36393f")
close.grid(row=8, column=2, columnspan=1)
img2 = PhotoImage(file="Images/close.png")
close.config(image=img2)

def clear():
    amount.set(1)
    delay.set(10)
    webhook.delete(0, 'end')
    message.delete(0, 'end')
    username.delete(0, 'end')

clear = Button(root, text="Clear", command=clear, borderwidth=0, background="#36393f")
clear.grid(row=7, column=2, columnspan=2)
img3 = PhotoImage(file="Images/clear.png")
clear.config(image=img3)

root.mainloop()