from asyncore import write
from tkinter import *
import sqlite3

root = Tk()
root.title("ADS")
width = 1000
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================VARIABLES======================================
AGE= StringVar()
MECHANISM = StringVar()
INJURY= StringVar()
SIGNSANDSYMPTOMS = StringVar()
TREATMENT= StringVar()

 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=800)
Form.pack(side=TOP, pady=5)


#==============================LABELS=========================================
lbl_title = Label(Top, text = "ADS", font=('Lato', 15))
lbl_title.pack(fill=X)
lbl_age = Label(Form, text = "Age:", font=('Lato', 10), bd=10)
lbl_age.grid(row=0, sticky="e")
lbl_mechanism= Label(Form, text = "Mechanism:", font=('Lato', 10), bd=15)
lbl_mechanism.grid(row=1, sticky="e")
lbl_injury = Label(Form, text = "Injury:", font=('Lato', 10), bd=15)
lbl_injury.grid(row=2, sticky="e")
lbl_ssymptoms= Label(Form, text = "Signs andSymptoms:", font=('Lato', 10), bd=15)
lbl_ssymptoms.grid(row=3, sticky="e")
lbl_treatment= Label(Form, text = "Treatment:", font=('Lato', 10), bd=10)
lbl_treatment.grid(row=4, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=3, columnspan=1)
 
#==============================ENTRY WIDGETS==================================
age = Entry(Form, textvariable=AGE, font=(14))
age.grid(row=0, column=1)
mechanism= Entry(Form, textvariable=MECHANISM, font=(14))
mechanism.grid(row=1, column=1)
injury = Entry(Form, textvariable=INJURY, font=(14))
injury.grid(row=2, column=1)
signs= Entry(Form, textvariable=SIGNSANDSYMPTOMS, font=(14))
signs.grid(row=3, column=1)
TREATMENT= Entry(Form, textvariable=TREATMENT, font=(14))
TREATMENT.grid(row=4, column=1)

#===========================DATABASE=========================================
#==============================METHODS========================================

#==============================BUTTON WIDGETS=================================
btn_submit = Button(Form, text="Submit", width=45, command=write)
btn_submit.grid(pady=25, row=5, columnspan=2)
btn_submit.bind('<Return>', write)

#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()
