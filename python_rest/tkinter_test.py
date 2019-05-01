from tkinter import *

master = Tk()
Label(master, text="Start Date").grid(row=0)
Label(master, text="End Date").grid(row=1)
Label(master, text="destination file path").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

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
    print("These items were selected")




mainloop( )