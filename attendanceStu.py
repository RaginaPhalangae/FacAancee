import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata=[]

class AttendanceStu:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #======================variables==================================================================

        # self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_department=StringVar()
        self.var_atten_status=StringVar()

        # first image
        img=Image.open(r"college_images\image2.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # second image

        img1=Image.open(r"college_images\image15.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg image

        img3=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image6.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT STSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times roman new",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=580)

        img_left=Image.open(r"college_images\image23.jpg")
        img_left=img_left.resize((770,175),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=770,height=175)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=180,width=770,height=310)

        #label and entries

        #Attendance id

        AttendanceID_label=Label(left_inside_frame,text="Roll No.:",font=("times roman new",13,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_roll,font=("times roman new",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Rollno

        Rollno_label=Label(left_inside_frame,text="Name:",font=("times roman new",13,"bold"),bg="white")
        Rollno_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Rollno_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_name,font=("times roman new",13,"bold"))
        Rollno_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name

        Name_label=Label(left_inside_frame,text="Department:",font=("times roman new",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_department,font=("times roman new",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department

        Department_label=Label(left_inside_frame,text="Time:",font=("times roman new",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Department_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_time,font=("times roman new",13,"bold"))
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time

        Time_label=Label(left_inside_frame,text="Date:",font=("times roman new",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_date,font=("times roman new",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date

        # Date_label=Label(left_inside_frame,text="Date:",font=("times roman new",13,"bold"),bg="white")
        # Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        # Date_entry=ttk.Entry(left_inside_frame,width=17,font=("times roman new",13,"bold"))
        # Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance

        attendanceStatus_label=Label(left_inside_frame,text="Attendance Status:",font=("times roman new",13,"bold"),bg="white")
        attendanceStatus_label.grid(row=2,column=2,padx=10,sticky=W)

        attendanceStatus_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_status,font=("times roman new",12,"bold"),width=15,state="readonly")
        attendanceStatus_combo["values"]=("Status","Present","Absent")
        attendanceStatus_combo.current(0)
        attendanceStatus_combo.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #button frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=270,width=755,height=35)

        Import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=24,font=("times roman new",13,"bold"),bg="darkblue",fg="white")
        Import_btn.grid(row=0,column=0)

        Export_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=24,font=("times roman new",13,"bold"),bg="green",fg="white")
        Export_btn.grid(row=0,column=1)

        # Update_btn=Button(btn_frame,text="Update",width=18,font=("times roman new",13,"bold"),bg="red",fg="white")
        # Update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=24,font=("times roman new",13,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3)


        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times roman new",12,"bold"))
        Right_frame.place(x=800,y=10,width=680,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=665,height=480)

        #Scroll bar and table=============================================================================================================================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        # self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=120)
        self.AttendanceReportTable.column("name",width=120)
        self.AttendanceReportTable.column("department",width=120)
        self.AttendanceReportTable.column("time",width=120)
        self.AttendanceReportTable.column("date",width=120)
        self.AttendanceReportTable.column("attendance",width=120)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #============================Fetching data=======================================================================================================

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File" ,"*.csv "),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File" ,"*.csv "),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_department.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_status.set(rows[5])

    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")





    


    
        



if __name__=="__main__":
    root=Tk()
    obj=AttendanceStu(root)
    root.mainloop()