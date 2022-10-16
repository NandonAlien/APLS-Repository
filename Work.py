from asyncore import write
from datetime import datetime
from tkinter import *
import sqlite3
import tkinter
from turtle import bgcolor

root = Tk()
root.title("ADS")
width = 1500
height = 600
root.configure(bg = 'orange')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(True, True)

#==============================VARIABLES======================================
IDNO = StringVar()
NAME = StringVar()
AGE= StringVar()
MECHANISM = StringVar()
INJURY= StringVar()
SIGNSANDSYMPTOMS = StringVar()
TREATMENT= StringVar()
EMT1 = StringVar()
EMT2 = StringVar()
AMBNO = StringVar()

 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=800,width=1000)
Form.pack(side=TOP, pady=5)


#==============================LABELS=========================================
lbl_title = Label(Top, text = "ADS", font=('Lato', 15))
lbl_title.pack(fill=X)
lbl_ID = Label(Form, text = "ID No.:", font=('Lato', 10), bd=10)
lbl_ID.grid(row=0, sticky="e", column=0)
lbl_name = Label(Form, text = "Name:", font=('Lato', 10), bd=10)
lbl_name.grid(row=0, sticky="e", column=2)
lbl_age = Label(Form, text = "Age:", font=('Lato', 10), bd=10)
lbl_age.grid(row=0, sticky="e", column=4)
lbl_mechanism= Label(Form, text = "Mechanism:", font=('Lato', 10), bd=15)
lbl_mechanism.grid(row=1, sticky="e")
lbl_injury = Label(Form, text = "Injury:", font=('Lato', 10), bd=15)
lbl_injury.grid(row=2, sticky="e")
lbl_ssymptoms= Label(Form, text = "Signs and --Symptoms:", font=('Lato', 10), bd=10)
lbl_ssymptoms.grid(row=3, sticky="e")
lbl_treatment= Label(Form, text = "Treatment:", font=('Lato', 10), bd=10)
lbl_treatment.grid(row=4, sticky="e")
lbl_emtFirst= Label(Form, text = "First responder 1:", font=('Lato', 10), bd=10)
lbl_emtFirst.grid(row=5, sticky="e", column = 0)
lbl_emtSecond= Label(Form, text = "First responder 2:", font=('Lato', 10), bd=10)
lbl_emtSecond.grid(row=5, sticky="e", column = 2)
lbl_AmbNO= Label(Form, text = "Ambulance License Plate:", font=('Lato', 10), bd=10)
lbl_AmbNO.grid(row=5, sticky="e", column = 4)
lbl_Empty= Label(Form, text = "", font=('Lato', 10), bd=10)
lbl_Empty.grid(row=5, sticky="e", column = 6)
lbl_text = Label(Form)
lbl_text.grid(row=3, columnspan=1, pady=4)
 
#==============================ENTRY WIDGETS==================================
IDNo = Entry(Form, textvariable=IDNO, font=(14))
IDNo.grid(row=0, column=1)
name = Entry(Form, textvariable=NAME, font=(14))
name.grid(row=0, column=3)
age = Entry(Form, textvariable=AGE, font=(14))
age.grid(row=0, column=5)
mechanism= Entry(Form, textvariable=MECHANISM, font=(14))
mechanism.grid(row=1, column=1)
injury = Entry(Form, textvariable=INJURY, font=(14))
injury.grid(row=2, column=1)
signs= Entry(Form, textvariable=SIGNSANDSYMPTOMS, font=(14))
signs.grid(row=3, column=1)
TREATMENT= Entry(Form, textvariable=TREATMENT, font=(14))
TREATMENT.grid(row=4, column=1)
Emt1= Entry(Form, textvariable=EMT1, font=(14))
Emt1.grid(row=5, column=1)
Emt2= Entry(Form, textvariable=EMT2, font=(14))
Emt2.grid(row=5, column=3)
AmbNO= Entry(Form, textvariable=AMBNO, font=(14))
AmbNO.grid(row=5, column=5)




#===========================DATABASE=========================================
#==============================METHODS========================================
def get_text():
    inp = "EMT notes from ambulance as of {date} : \n" . format(date = datetime.now())
    inp += "Patient ID: {ID} \n" . format(ID = IDNo.get())
    inp += "Patient name: {Name}\n" . format(Name = name.get())
    inp += "Patient age: {Age}\n" . format(Age = age.get())
    inp += "Patient mechanism of injury: {Mechanism} \n" . format(Mechanism = mechanism.get())
    inp += "Patient injury : {Injury} \n" . format(Injury = injury.get())
    inp += "Patient signs/symptoms: {Signs}\n" . format(Signs = signs.get())
    inp += "Treatments administered to patient by EMT: {Treatments}\n" . format(Treatments = TREATMENT.get())
    inp += "First responder (1): {EMT1} \n" . format(EMT1 = Emt1.get())
    inp += "First responder (2): {EMT2} \n" . format(EMT2 = Emt2.get())
    inp += "Ambulance License Plate: {AmbPlate} \n\n" . format(AmbPlate = AmbNO.get())

    #print(inp)
    with open("myfile.txt", "a") as file:
      file.write(inp)
      print('saved')
      file = open("myfile.txt", "r")
      print(file.read())
   # file.close()
   # file.write(inp)
      
#==============================BUTTON WIDGETS=================================
#file_name = mechanism.get("1.0", END)
btn_submit = Button(Form, text="Submit", width=45, command=get_text)
btn_submit.grid(pady=25, row=6, columnspan=6)
btn_submit.bind('<Return>', write)

#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()