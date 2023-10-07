from PLL import Image, ImageTK
from tkinter import TK, Lable, BOTH
from tkinter.tkk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI ()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("Z:\\Courses\\Python\\rotunda.jpg")
        bard=bard.resize((100,100),Image.ANTIALIAS)
        bardejov = ImageTK.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot=Image.open("Z:\\Courses\\Python\\rotunda.jpg")
        rot=rot.resize((100,100),Image.ANTIALIAS)
        rotunda = ImageTK.PhotoImage(rot)
        label2 =Lable(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)
        
        minc = Image.open("Z:\\Courses\\Python\\mincol.jpg")
        minc=minc.resize((100,100),Image.ANTIALIAS)
        mincol = ImageTK.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)

    root =Tk()
    root.geometry("300x280+300+300")
    app =Example(root)
    root.mainloop()