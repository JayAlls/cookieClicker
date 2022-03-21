from tkinter import *

window = Tk()
window.title("Simply Clickers !")
window.geometry("720x480")
window.minsize(720, 480)
window.config(bg="#cb997e")

# Gros titre

title = Label(window, text="SIMPLY CLICKERS", bg="#cb997e", font=("Times", 30))
title.pack(side=TOP)

# FUNCTION
cookie = 0


def add_cookie():
    global cookie
    cookie += 1
    count_click.config(text=cookie)


def add_cookie2():
    global cookie
    cookie *= 2
    count_click.config(text=cookie)


def add_cookie3():
    global cookie
    cookie *= 3
    count_click.config(text=cookie)


def add_cookie5():
    global cookie
    cookie *= 5
    count_click.config(text=cookie)



# Boîte à Clickers
left_frame = Frame(window, bg="#cb997e")


# Compteur de click
count_click = Label(left_frame, text='0', bg='#cb997e', font=('Arial', 35), fg='white')
count_click.pack()

# Cookies
width = 300
height = 300
cookie_img = PhotoImage(file="gingerbread.png").zoom(13).subsample(32)
clickers = Button(left_frame, image=cookie_img, relief=SUNKEN, bg="#cb997e", bd=0, command=add_cookie, cursor="tcross")
clickers.pack()

# Boutique

right_frame = Frame(window, bg="#cb997e")

# Options

double = Label(right_frame, text="10CK = Click x2", bg="#cb997e", font=("Arial", 20), fg="white")
triple = Label(right_frame, text="30CK = Click x3", bg="#cb997e", font=("Arial", 20), fg="white")
cinqtuple = Label(right_frame, text="1000CK = Click x3", bg="#cb997e", font=("Arial", 20),fg="white")
double.pack()
triple.pack()
cinqtuple.pack()


right_frame.pack(side=RIGHT)
left_frame.pack(side=LEFT)
window.mainloop()
