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


# Boîte à Clickers
middle_frame = Frame(window, bg="#cb997e")


# Compteur de click
count_click = Label(middle_frame, text='0', bg='#cb997e', font=('Arial', 35), fg='white')
count_click.pack()

# Cookies
width = 300
height = 300
cookie_img = PhotoImage(file="gingerbread.png").zoom(13).subsample(32)
clickers = Button(middle_frame, image=cookie_img, relief=SUNKEN, bg="#cb997e", bd=0, command=add_cookie, cursor="tcross")
clickers.pack()

middle_frame.pack(expand=YES)
window.mainloop()
