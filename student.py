import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #====================variables====================================================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

        # first image
        img=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image2.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image

        img1=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image15.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        # third image

        img2=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image14.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image

        img3=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image6.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT STSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times roman new",12,"bold"))
        Left_frame.place(x=10,y=10,width=780,height=580)

        img_left=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image17.jpg")
        img_left=img_left.resize((770,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=770,height=130)

        #Current course Information

        Current_Course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times roman new",12,"bold"))
        Current_Course.place(x=5,y=135,width=770,height=130)

        #Department

        dep_label=Label(Current_Course,text="Department",font=("times roman new",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(Current_Course,textvariable=self.var_dep,font=("times roman new",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Information Technology","Computer Science","Computer Science and Artificial Intelligence", "Computer Science and Business")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course

        Course_label=Label(Current_Course,text="Course",font=("times roman new",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_Course,textvariable=self.var_course,font=("times roman new",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","P.Hd","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year

        year_label=Label(Current_Course,text="Year",font=("times roman new",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_Course,textvariable=self.var_year,font=("times roman new",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-2024","2021-2025","2022-2026","2023-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester

        Semester_label=Label(Current_Course,text="Semester",font=("times roman new",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        Semester_combo=ttk.Combobox(Current_Course,textvariable=self.var_semester,font=("times roman new",12,"bold"),width=17,state="readonly")
        Semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        
        #class student information

        Class_student=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times roman new",12,"bold"))
        Class_student.place(x=5,y=270,width=770,height=285)

        #Student Id

        StuddentID_label=Label(Class_student,text="Student ID:",font=("times roman new",13,"bold"),bg="white")
        StuddentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(Class_student,textvariable=self.var_id,width=17,font=("times roman new",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name

        StuddentName_label=Label(Class_student,text="Student Name:",font=("times roman new",13,"bold"),bg="white")
        StuddentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(Class_student,textvariable=self.var_name,width=17,font=("times roman new",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Address

        Address_label=Label(Class_student,text="Address:",font=("times roman new",13,"bold"),bg="white")
        Address_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_student,textvariable=self.var_address,width=17,font=("times roman new",13,"bold"))
        Address_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll number

        Rollno_label=Label(Class_student,text="Roll Number:",font=("times roman new",13,"bold"),bg="white")
        Rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(Class_student,textvariable=self.var_rollno,width=17,font=("times roman new",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender

        gender_label=Label(Class_student,text="Gender:",font=("times roman new",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(Class_student,textvariable=self.var_gender,width=17,font=("times roman new",13,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_student,textvariable=self.var_gender,font=("times roman new",12,"bold"),width=15,state="readonly")
        gender_combo["values"]=("Select","Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #DOB

        dob_label=Label(Class_student,text="Date of Birth:",font=("times roman new",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(Class_student,textvariable=self.var_dob,width=17,font=("times roman new",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email

        email_label=Label(Class_student,text="Email:",font=("times roman new",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Class_student,textvariable=self.var_email,width=17,font=("times roman new",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone

        phone_label=Label(Class_student,text="Phone Number:",font=("times roman new",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(Class_student,textvariable=self.var_phone,width=17,font=("times roman new",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_student,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=5)

        radiobtn2=ttk.Radiobutton(Class_student,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=5)

        #button frame

        btn_frame=Frame(Class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=185,width=755,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times roman new",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times roman new",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times roman new",13,"bold"),bg="red",fg="white")
        Delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times roman new",13,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3)


        #take photo frame

        btn_frame1=Frame(Class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=220,width=755,height=35)

        
        takephoto_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=37,font=("times roman new",13,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=37,font=("times roman new",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=1)
        

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times roman new",12,"bold"))
        Right_frame.place(x=800,y=10,width=680,height=580)

        img_right=Image.open(r"C:\Users\ayush\Desktop\Fa\college_images\image18.jpg")
        img_right=img_right.resize((770,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=770,height=130)



        # =====================================Search System============================================================================================================================


        #class student information

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times roman new",12,"bold"))
        Search_frame.place(x=5,y=135,width=670,height=65)

        #search by

        search_label=Label(Search_frame,text="Search By:",font=("times roman new",12,"bold"),bg="darkred",fg="white",width=10)
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times roman new",12,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times roman new",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Serach_btn=Button(Search_frame,text="Search",width=10,font=("times roman new",12,"bold"),bg="green",fg="white")
        Serach_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        Showall_btn=Button(Search_frame,text="Show All",width=10,font=("times roman new",12,"bold"),bg="purple",fg="white")
        Showall_btn.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        #Table frame

        Table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=670,height=345)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","rollno","gender","DOB","Email","Phone","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="Photo Sample Status")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #=============================Function Declaration===============================================================

    def add_data(self):
        if self.var_dep.get()=="Select Department"  or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Required field is not filled!",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_rollno.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details are stored!",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #===========================Fetch Data=======================================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=================get cursor===========================================================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_rollno.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])

    #=====================update function========================================================

    def update_data(self):
        if self.var_dep.get()=="Select Department"  or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Required field is not filled!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Rollno=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo_Sample_Status=%s WHERE Student_ID=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_rollno.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_radio1.get(),self.var_id.get()))
                
                else:
                    if not Update:                                                                                                                                                                                                                                                                                                                                                  
                        return
                messagebox.showinfo("Success","Student's Details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #===================delete function===============================================================================================================================================================================================

    def delete_data(self):
        if self.var_id.get=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student's details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #===============================Reset Function===================================================================================================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    #==========================Generate Data set or Take photo samples================================================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"  or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Required field is not filled!",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Rollno=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Photo_Sample_Status=%s WHERE Student_ID=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                        self.var_rollno.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_id.get()==id+1
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                # numm =  self.var_id.get()
                self.reset_data()
                conn.close()

                #==================Load pre defined data from openCv=============================================================================================================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for(x,y,z,w) in faces:
                        face_cropped=img[y:y+w,x:x+z]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi@9683",database="face_recognizer")
                        # # my_cursor=conn.cursor()
                        # numm = self.var_id.get()
                        # nameee = self.var_name.get()



                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed Successfully!")


            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)










                

        
        



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()