from tkinter import *



def grab(start_date, end_date, file_path):
    pass


master = Tk()

master.title("Aqueduct Data")
master.geometry('1300x200')

Label(master, text="Start Year").grid(row=0)
Label(master, text="Start Month").grid(row=1)
Label(master, text="End Year").grid(row=2)
Label(master, text="End Month").grid(row=3)
Label(master, text="destination file path").grid(row=4)

start_date = Entry(master)
end_date = Entry(master)
file_path = Entry(master)
start_month = Entry(master)
end_month = Entry(master)

start_date.grid(row=0, column=1)
start_month.grid(row=1, column=1)
end_date.grid(row=2,column=1)
end_month.grid(row=3,column=1)
file_path.grid(row=4,column=1)

Res = IntVar()
solids= IntVar()
NTU = IntVar()
org_ml= IntVar()
tc_MPN = IntVar()
ec_MPN= IntVar()
LosR = IntVar()
Silica= IntVar()
Ca = IntVar()
Mg= IntVar()
Ca_Mg = IntVar()

NO3= IntVar()
USGS_NO3= IntVar()
C12 = IntVar()
Na= IntVar()
SO4 = IntVar()
K= IntVar()
pH = IntVar()
Alk= IntVar()
Hard= IntVar()
Nhard= IntVar()
C_USGS_Temp= IntVar()

F_USGS= IntVar()
Temp= IntVar()
MD_precip= IntVar()
MD_Temp= IntVar()


Checkbutton(master, text="Res",variable=Res).grid(row=0, column=4)
Checkbutton(master, text="solids", variable=solids).grid(row=0, column=5)
Checkbutton(master, text="NTU",variable=NTU).grid(row=0, column=6)
Checkbutton(master, text="org/ml", variable=org_ml).grid(row=0, column=7)
Checkbutton(master, text="total coliform MPN/100ml",variable=tc_MPN).grid(row=0, column=8)
Checkbutton(master, text="E coli MPN/100ml", variable=ec_MPN).grid(row=0, column=9)
Checkbutton(master, text="LosR",variable=LosR).grid(row=0, column=10)
Checkbutton(master, text="Silica", variable=Silica).grid(row=0, column=11)
Checkbutton(master, text="Ca", variable=Ca).grid(row=0, column=12)
Checkbutton(master, text="Mg",variable=Mg).grid(row=0, column=13)
Checkbutton(master, text="Ca+Mg", variable=Ca_Mg).grid(row=0, column=14)

Checkbutton(master, text="NO3",variable=NO3).grid(row=1, column=4)
Checkbutton(master, text="USGS NO3", variable=USGS_NO3).grid(row=1, column=5)
Checkbutton(master, text="C12",variable=C12).grid(row=1, column=6)
Checkbutton(master, text="Na", variable=Na).grid(row=1, column=7)
Checkbutton(master, text="SO4",variable=SO4).grid(row=1, column=8)
Checkbutton(master, text="K", variable=K).grid(row=1, column=9)
Checkbutton(master, text="pH",variable=pH).grid(row=1, column=10)
Checkbutton(master, text="Alk", variable=Alk).grid(row=1, column=11)
Checkbutton(master, text="Hard", variable=Hard).grid(row=1, column=12)
Checkbutton(master, text="Nhard",variable=Nhard).grid(row=1, column=13)
Checkbutton(master, text="C USGS Temp", variable=C_USGS_Temp).grid(row=1, column=14)

Checkbutton(master, text="F USGS",variable=F_USGS).grid(row=2, column=4)
Checkbutton(master, text="Temp", variable=Temp).grid(row=2, column=5)
Checkbutton(master, text="MD Precip inch/mon",variable=MD_precip).grid(row=2, column=6)
Checkbutton(master, text="MD Temp F", variable=MD_Temp).grid(row=2, column=7)

def write_selections():
    sd =(start_date.get())
    sm = (start_month.get())
    ed = (end_date.get())
    em = (end_month.get())
    path =(file_path.get())

    print(sd, sm, ed, em, path)
    return (sd, sm, ed, em, path)



#feed selections into array then json file?

button=Button(master, text="Download Data", bg="blue", fg="white", command=write_selections)
button.grid(column=7, row=5)






mainloop( )
