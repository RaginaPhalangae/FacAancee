import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\image24.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)

        img_top_1=Image.open(r"college_images\Ayushi3.jpeg")
        img_top_1=img_top_1.resize((200,250),Image.ANTIALIAS)
        self.photoimg_top_1=ImageTk.PhotoImage(img_top_1)

        f_lbl=Label(main_frame,image=self.photoimg_top_1)
        f_lbl.place(x=300,y=0,width=200,height=250)

        dep_label=Label(main_frame,text="Hi, My name is Ayushi",font=("times roman new",20,"bold"),bg="white",fg="darkblue")
        dep_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="I am the ownwer.",font=("times roman new",20,"bold"),bg="white",fg="darkblue")
        dep_label.place(x=0,y=40)

        img_top_2=Image.open(r"college_images\image25.jpg")
        img_top_2=img_top_2.resize((500,320),Image.ANTIALIAS)
        self.photoimg_top_2=ImageTk.PhotoImage(img_top_2)

        f_lbl=Label(main_frame,image=self.photoimg_top_2)
        f_lbl.place(x=0,y=270,width=500,height=320)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()