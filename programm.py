from tkinter import *
from tkinter.ttk import *

w=Tk()
w.title("Yokai-Serverüberwachung")
w.attributes("-fullscreen", True)

style = Style()

style.configure ("W.TButton", font = 
                ("Bebas", 20, "bold", "underline"),
                fg = "ba2323")


buttonE = Button(w,
                text='Exit!',
                style = "W.TButton",
                font=('Bebas', '30'),
                command=sys.exit,
                fg="#ba2323",
                bg="#201f1f",
                )
buttonE.grid(row = 0, column =3, padx = 100)
buttonE.place(x=800, y=800)
buttonE.config( width=250, height=250)
buttonE.pack()

w.mainloop()