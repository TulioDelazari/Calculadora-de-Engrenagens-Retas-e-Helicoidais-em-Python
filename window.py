from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("882x555")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 555,
    width = 882,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    441.0, 277.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    661.5, 350.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry0.place(
    x = 487, y = 210,
    width = 349,
    height = 278)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    209.0, 98.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry1.place(
    x = 75, y = 80,
    width = 268,
    height = 35)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    209.0, 467.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry2.place(
    x = 75, y = 444,
    width = 268,
    height = 44)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    209.0, 246.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry3.place(
    x = 75, y = 231,
    width = 268,
    height = 29)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    209.0, 366.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry4.place(
    x = 75, y = 351,
    width = 268,
    height = 29)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    209.0, 306.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry5.place(
    x = 75, y = 291,
    width = 268,
    height = 29)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    209.0, 186.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry6.place(
    x = 75, y = 171,
    width = 268,
    height = 29)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 133, y = 507,
    width = 151,
    height = 36)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    662.0, 520.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry7.place(
    x = 546, y = 505,
    width = 232,
    height = 29)

window.resizable(False, False)
window.mainloop()
