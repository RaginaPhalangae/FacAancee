import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector













class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\image26.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dep_label=Label(self.root,text="Email:rphalangae@gmail.com",font=("times roman new",20,"bold"),bg="white",fg="darkblue")
        dep_label.place(x=600,y=400)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()