# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:46:40 2023

@author: vedantjitendrabhaip
"""

from tkinter import filedialog, messagebox
from tkinter import *
import random
import time


def reset():    
    
    textReceipt.delete(1.0, END)
    
    e_roti.set('0')
    e_daal.set('0')
    e_rice.set('0')
    e_chhole.set('0')
    e_rajma.set('0')
    e_sahipaneer.set('0')
    e_dosa.set('0')
    e_pavbhaji.set('0')
    e_dalbaati.set('0')
    
    e_lassi.set('0')
    e_faluda.set('0')
    e_buttermilk.set('0')
    e_roohafza.set('0')
    e_masalatea.set('0')
    e_coldcoffee.set('0')
    e_almondmilk.set('0')
    e_sugarcanejuice.set('0')
    e_jaljeera.set('0')

    e_gulabjamun.set('0')
    e_carrothalva.set('0')
    e_jalebi.set('0')
    e_rasgulla.set('0')
    e_rasmalai.set('0')
    e_rabdi.set('0')
    e_shrikhand.set('0')
    e_barfi.set('0')
    e_kheer.set('0')
    
    
    textroti.config(state = DISABLED)
    textdaal.config(state = DISABLED)
    textrice.config(state = DISABLED)
    textchhole.config(state = DISABLED)
    textrajma.config(state = DISABLED)
    textsahipaneer.config(state = DISABLED)
    textdosa.config(state = DISABLED)
    textpavbhaji.config(state = DISABLED)
    textdalbaati.config(state = DISABLED)
    
    textlassi.config(state = DISABLED)
    textfaluda.config(state = DISABLED)
    textbuttermilk.config(state = DISABLED)
    textroohafza.config(state = DISABLED)
    textmasalatea.config(state = DISABLED)
    textcoldcoffee.config(state = DISABLED)
    textalmondmilk.config(state = DISABLED)
    textsugarcanejuice.config(state = DISABLED)
    textjaljeera.config(state = DISABLED)
    
    textgulabjamun.config(state = DISABLED)
    textcarrothalva.config(state = DISABLED)
    textjalebi.config(state = DISABLED)
    textrasgulla.config(state = DISABLED)
    textrasmalai.config(state = DISABLED)
    textrabdi.config(state = DISABLED)
    textshrikhand.config(state = DISABLED)
    textbarfi.config(state = DISABLED)
    textkheer.config(state = DISABLED)
    
    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofdessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill is Sucessfully Saved!!!')
    

def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofdrinksvar.get() != '' or costofdessertvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t'.expandtabs(16)+date+'\n')
        textReceipt.insert(END,'************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost of Items(CAD)\n')
        textReceipt.insert(END,'************************************************************\n')
        
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*2}\n\n')
        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*12}\n\n')
        if e_rice.get()!='0':
            textReceipt.insert(END,f'Rice\t\t\t{int(e_rice.get())*10}\n\n')
        if e_chhole.get()!='0':
            textReceipt.insert(END,f'Chhole\t\t\t{int(e_chhole.get())*15}\n\n')    
        if e_rajma.get()!='0':
            textReceipt.insert(END,f'Rajma\t\t\t{int(e_rajma.get())*15}\n\n')
        if e_sahipaneer.get()!='0':
             textReceipt.insert(END,f'Sahi Paneer\t\t\t{int(e_sahipaneer.get())*15}\n\n')
        if e_dosa.get()!='0':
            textReceipt.insert(END,f'Dosa\t\t\t{int(e_dosa.get())*20}\n\n')
        if e_pavbhaji.get()!='0':
            textReceipt.insert(END,f'Pav Bhaji\t\t\t{int(e_pavbhaji.get())*15}\n\n')
        if e_dalbaati.get()!='0':
            textReceipt.insert(END,f'Dal Baati\t\t\t{int(e_dalbaati.get())*20}\n\n') 
            
        if e_lassi.get()!='0':
            textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*8}\n\n')
        if e_faluda.get()!='0':
            textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*8}\n\n')    
        if e_buttermilk.get()!='0':
             textReceipt.insert(END,f'Butter Milk\t\t\t{int(e_buttermilk.get())*5}\n\n')
        if e_roohafza.get()!='0':
            textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*5}\n\n')
        if e_masalatea.get()!='0':
            textReceipt.insert(END,f'Masalatea\t\t\t{int(e_masalatea.get())*8}\n\n')
        if e_coldcoffee.get()!='0':
            textReceipt.insert(END,f'Coldcoffee\t\t\t{int(e_coldcoffee.get())*6}\n\n')
        if e_almondmilk.get()!='0':
            textReceipt.insert(END,f'Almondmilk\t\t\t{int(e_almondmilk.get())*7}\n\n')
        if e_sugarcanejuice.get()!='0':
            textReceipt.insert(END,f'Sugar-Cane Juice\t\t\t{int(e_sugarcanejuice.get())*8}\n\n')     
        if e_jaljeera.get()!='0':
            textReceipt.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*5}\n\n')
        
        if e_gulabjamun.get()!='0':
            textReceipt.insert(END,f'Gulabjamun\t\t\t{int(e_gulabjamun.get())*10}\n\n')
        if e_carrothalva.get()!='0':
             textReceipt.insert(END,f'Carrot Halva\t\t\t{int(e_carrothalva.get())*12}\n\n')
        if e_jalebi.get()!='0':
            textReceipt.insert(END,f'Jalebi\t\t\t{int(e_jalebi.get())*8}\n\n')
        if e_rasgulla.get()!='0':
            textReceipt.insert(END,f'Rasgulla\t\t\t{int(e_rasgulla.get())*8}\n\n')    
        if e_rasmalai.get()!='0':
            textReceipt.insert(END,f'Rasmalai\t\t\t{int(e_rasmalai.get())*10}\n\n')
        if e_rabdi.get()!='0':
            textReceipt.insert(END,f'rabdi\t\t\t{int(e_rabdi.get())*8}\n\n')
        if e_shrikhand.get()!='0':
            textReceipt.insert(END,f'Shrikhand\t\t\t{int(e_shrikhand.get())*10}\n\n')
        if e_barfi.get()!='0':
            textReceipt.insert(END,f'Barfi\t\t\t{int(e_barfi.get())*8}\n\n')
        if e_kheer.get()!='0':
            textReceipt.insert(END,f'Kheer\t\t\t{int(e_kheer.get())*10}\n\n')
        
        
        textReceipt.insert(END,'************************************************************\n')
        
        if costoffoodvar.get()!='0 CAD':
            textReceipt.insert(END,f'Cost of Food\t\t\t{priceofFood}CAD\n\n')
        
        if costoffoodvar.get()!='0 CAD':
            textReceipt.insert(END,f'Cost of Drinks\t\t\t{priceofDrinks}CAD\n\n')
        
        if costoffoodvar.get()!='0 CAD':
            textReceipt.insert(END,f'Cost of Dessert\t\t\t{priceofDessert}CAD\n\n')
        
        textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofitems}CAD\n\n')
        textReceipt.insert(END,f'Service Tax\t\t\t{5}CAD\n\n')
        textReceipt.insert(END,f'Total Cost\t\t\t{subtotalofitems+5}CAD\n\n')
        
        textReceipt.insert(END,'************************************************************\n')
    
    else:
        messagebox.showerror('Error','No item is selected')
        
def totalcost():
    global priceofFood,priceofDrinks,priceofDessert,subtotalofitems
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or \
       var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or \
       var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or \
       var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or \
       var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or \
       var26.get()!=0 or var27.get()!=0:
        item1=int(e_roti.get())
        item2=int(e_daal.get())
        item3=int(e_rice.get())
        item4=int(e_chhole.get())
        item5=int(e_rajma.get())
        item6=int(e_sahipaneer.get())
        item7=int(e_dosa.get())
        item8=int(e_pavbhaji.get())
        item9=int(e_dalbaati.get())
        
        item10=int(e_lassi.get())
        item11=int(e_faluda.get())
        item12=int(e_buttermilk.get())
        item13=int(e_roohafza.get())
        item14=int(e_masalatea.get())
        item15=int(e_coldcoffee.get())
        item16=int(e_almondmilk.get())
        item17=int(e_sugarcanejuice.get())
        item18=int(e_jaljeera.get())
        
        item19=int(e_gulabjamun.get())
        item20=int(e_carrothalva.get())
        item21=int(e_jalebi.get())
        item22=int(e_rasgulla.get())
        item23=int(e_rasmalai.get())
        item24=int(e_rabdi.get())
        item25=int(e_shrikhand.get())
        item26=int(e_barfi.get())
        item27=int(e_kheer.get())
        
        priceofFood = (item1 * 2) + (item2 * 12) + (item3 * 10) + (item4 * 15) + (item5 * 15) + (item6 * 15) + (item7 * 20) + (item8 * 15) + (item9 * 20)
        
        priceofDrinks = (item10 * 8) + (item11 * 8) + (item12 * 5) + (item13 * 5) + (item14 * 8) + (item15 * 6) + (item16 * 7) + (item17 * 8) + (item18 * 5)
                      
        priceofDessert = (item19 * 10) + (item20 * 12) + (item21 * 8) + (item22 * 8) + (item23 * 10) + (item24 * 8) + (item25 * 10) + (item26 * 8) + (item27 * 10)
        
        costoffoodvar.set(str(priceofFood)+ ' CAD')
        costofdrinksvar.set(str(priceofDrinks)+ ' CAD')
        costofdessertvar.set(str(priceofDessert)+ ' CAD')
        
        subtotalofitems=priceofFood+priceofDrinks+priceofDessert
        subtotalvar.set(str(subtotalofitems)+ ' CAD')
        
        servicetaxvar.set('5 CAD')
        
        tottalcost = subtotalofitems + 5
        totalcostvar.set(str(tottalcost)+ ' CAD')
    
    else:
        messagebox.showerror('Error', 'No item is Selected, Please Select at least One Item.')
        
    
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()    
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()   
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def rice():
    if var3.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()   
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')

def chhole():
    if var4.get()==1:
        textchhole.config(state=NORMAL)
        textchhole.delete(0,END)
        textchhole.focus()   
    else:
        textchhole.config(state=DISABLED)
        e_chhole.set('0')

def rajma():
    if var5.get()==1:
        textrajma.config(state=NORMAL)
        textrajma.delete(0,END)
        textrajma.focus()   
    else:
        textrajma.config(state=DISABLED)
        e_rajma.set('0')

def sahipaneer():
    if var6.get()==1:
        textsahipaneer.config(state=NORMAL)
        textsahipaneer.delete(0,END)
        textsahipaneer.focus()   
    else:
        textsahipaneer.config(state=DISABLED)
        e_sahipaneer.set('0')
        
def dosa():
    if var7.get()==1:
        textdosa.config(state=NORMAL)
        textdosa.delete(0,END)
        textdosa.focus()   
    else:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')
        
def pavbhaji():
    if var8.get()==1:
        textpavbhaji.config(state=NORMAL)
        textpavbhaji.delete(0,END)
        textpavbhaji.focus()   
    else:
        textpavbhaji.config(state=DISABLED)
        e_pavbhaji.set('0')

def dalbaati():
    if var9.get()==1:
        textdalbaati.config(state=NORMAL)
        textdalbaati.delete(0,END)
        textdalbaati.focus()   
    else:
        textdalbaati.config(state=DISABLED)
        e_dalbaati.set('0')



def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()   
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def faluda():
    if var11.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()   
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def buttermilk():
    if var12.get()==1:
        textbuttermilk.config(state=NORMAL)
        textbuttermilk.delete(0,END)
        textbuttermilk.focus()   
    else:
        textbuttermilk.config(state=DISABLED)
        e_buttermilk.set('0')

def roohafza():
    if var13.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()   
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')

def masalatea():
    if var14.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()   
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')

def coldcoffee():
    if var15.get()==1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.delete(0,END)
        textcoldcoffee.focus()   
    else:
        textcoldcoffee.config(state=DISABLED)
        e_coldcoffee.set('0')
        
def almondmilk():
    if var16.get()==1:
        textalmondmilk.config(state=NORMAL)
        textalmondmilk.delete(0,END)
        textalmondmilk.focus()   
    else:
        textalmondmilk.config(state=DISABLED)
        e_almondmilk.set('0')

def sugarcanejuice():
    if var17.get()==1:
        textsugarcanejuice.config(state=NORMAL)
        textsugarcanejuice.delete(0,END)
        textsugarcanejuice.focus()   
    else:
        textsugarcanejuice.config(state=DISABLED)
        e_sugarcanejuice.set('0')
        
def jaljeera():
    if var18.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()   
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

        
def gulabjamun():
    if var19.get()==1:
        textgulabjamun.config(state=NORMAL)
        textgulabjamun.delete(0,END)
        textgulabjamun.focus()   
    else:
        textgulabjamun.config(state=DISABLED)
        e_gulabjamun.set('0')

def carrothalva():
    if var20.get()==1:
        textcarrothalva.config(state=NORMAL)
        textcarrothalva.delete(0,END)
        textcarrothalva.focus()   
    else:
        textcarrothalva.config(state=DISABLED)
        e_carrothalva.set('0')

def jalebi():
    if var21.get()==1:
        textjalebi.config(state=NORMAL)
        textjalebi.delete(0,END)
        textjalebi.focus()   
    else:
        textjalebi.config(state=DISABLED)
        e_jalebi.set('0')
        
def rasgulla():
    if var22.get()==1:
        textrasgulla.config(state=NORMAL)
        textrasgulla.delete(0,END)
        textrasgulla.focus()   
    else:
        textrasgulla.config(state=DISABLED)
        e_rasgulla.set('0')
        
def rasmalai():
    if var23.get()==1:
        textrasmalai.config(state=NORMAL)
        textrasmalai.delete(0,END)
        textrasmalai.focus()   
    else:
        textrasmalai.config(state=DISABLED)
        e_rasmalai.set('0')

def rabdi():
    if var24.get()==1:
        textrabdi.config(state=NORMAL)
        textrabdi.delete(0,END)
        textrabdi.focus()   
    else:
        textrabdi.config(state=DISABLED)
        e_rabdi.set('0')

def shrikhand():
    if var25.get()==1:
        textshrikhand.config(state=NORMAL)
        textshrikhand.delete(0,END)
        textshrikhand.focus()   
    else:
        textshrikhand.config(state=DISABLED)
        e_shrikhand.set('0')

def barfi():
    if var26.get()==1:
        textbarfi.config(state=NORMAL)
        textbarfi.delete(0,END)
        textbarfi.focus()   
    else:
        textbarfi.config(state=DISABLED)
        e_barfi.set('0')

def kheer():
    if var27.get()==1:
        textkheer.config(state=NORMAL)
        textkheer.delete(0,END)
        textkheer.focus()   
    else:
        textkheer.config(state=DISABLED)
        e_kheer.set('0')




root=Tk()

root.geometry('1334x710+0+0') # Size of the Window
root.resizable(0,0) # To stop maximizing the window
root.title('MenuMaster - A Restaurant Menu Ordering System (By Vedant Patel)') # Title of the Window
root.config(bg='skyblue') # Background Color


# Creating a Frame at Top position of the seceen
titleFrame = Frame(root, bd = 12, relief = RIDGE, bg = 'crimson')
titleFrame.pack(side = TOP)

labelTitle = Label(titleFrame, text='Royal Indian Food Palace', font = ('arial', 28, 'bold'), fg = 'yellow', bd = 10 , bg = 'gray', width = 56)
labelTitle.grid(row = 0, column = 0)


# Creating Frames
menuFrame = Frame(root, bd = 10, relief = RIDGE, bg = 'crimson')
menuFrame.pack(side = LEFT)

costFrame = Frame(menuFrame, bd = 8, relief = RIDGE, bg = 'antiquewhite2', padx = 17, pady = 12)
costFrame.pack(side = BOTTOM)

foodFrame = LabelFrame(menuFrame, text = 'Food', font = ('ariel', 18, 'bold'), bd = 8, relief = RIDGE, fg = 'crimson')
foodFrame.pack(side = LEFT)

drinksFrame = LabelFrame(menuFrame, text = 'Drinks', font = ('ariel', 18, 'bold'), bd = 8, relief = RIDGE, fg = 'crimson')
drinksFrame.pack(side = LEFT)

dessertFrame = LabelFrame(menuFrame, text = 'Desserts', font=('ariel', 18, 'bold'), bd = 8, relief = RIDGE, fg = 'crimson')
dessertFrame.pack(side = LEFT)

rightFrame = Frame(root, bd = 10, relief = RIDGE, bg = 'crimson')
rightFrame.pack(side = RIGHT)

calculatorFrame = Frame(rightFrame, bd = 8, relief = RIDGE, bg = 'darkorange2')
calculatorFrame.pack()

receiptFrame = Frame(rightFrame, bd = 8, relief = RIDGE, bg = 'blue2')
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd = 8, relief = RIDGE, bg = 'forestgreen')
buttonFrame.pack()



# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_rice = StringVar()
e_chhole = StringVar()
e_rajma = StringVar()
e_sahipaneer = StringVar()
e_dosa = StringVar()
e_pavbhaji = StringVar()
e_dalbaati = StringVar()

e_lassi = StringVar()
e_faluda = StringVar()
e_buttermilk = StringVar()
e_roohafza=StringVar()
e_masalatea=StringVar()
e_coldcoffee = StringVar()
e_almondmilk = StringVar()
e_sugarcanejuice = StringVar()
e_jaljeera = StringVar()

e_gulabjamun = StringVar()
e_carrothalva = StringVar()
e_jalebi = StringVar()
e_rasgulla = StringVar()
e_rasmalai = StringVar()
e_rabdi = StringVar()
e_shrikhand = StringVar()
e_barfi = StringVar()
e_kheer = StringVar()


e_roti.set('0')
e_daal.set('0')
e_rice.set('0')
e_chhole.set('0')
e_rajma.set('0')
e_sahipaneer.set('0')
e_dosa.set('0')
e_pavbhaji.set('0')
e_dalbaati.set('0')

e_lassi.set('0')
e_faluda.set('0')
e_buttermilk.set('0')
e_roohafza.set('0')
e_masalatea.set('0')
e_coldcoffee.set('0')
e_almondmilk.set('0')
e_sugarcanejuice.set('0')
e_jaljeera.set('0')

e_gulabjamun.set('0')
e_carrothalva.set('0')
e_jalebi.set('0')
e_rasgulla.set('0')
e_rasmalai.set('0')
e_rabdi.set('0')
e_shrikhand.set('0')
e_barfi.set('0')
e_kheer.set('0')

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofdessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()



# Food

roti = Checkbutton(foodFrame, text = 'Roti', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var1, command = roti)
roti.grid(row = 0, column = 0, sticky = W)

daal = Checkbutton(foodFrame, text = 'Daal', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var2, command = daal)
daal.grid(row = 1, column = 0, sticky = W)

rice = Checkbutton(foodFrame, text = 'Rice', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var3, command = rice)
rice.grid(row = 2, column = 0, sticky = W)

chhole = Checkbutton(foodFrame, text = 'Chhole', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var4, command = chhole)
chhole.grid(row = 3, column = 0, sticky = W)

rajma = Checkbutton(foodFrame, text = 'Rajma', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var5, command = rajma)
rajma.grid(row = 4, column = 0, sticky = W)

sahipaneer = Checkbutton(foodFrame, text = 'Sahi Paneer', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var6, command = sahipaneer)
sahipaneer.grid(row = 5, column = 0, sticky = W)

dosa = Checkbutton(foodFrame, text = 'Dosa', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var7, command = dosa)
dosa.grid(row = 6,column = 0, sticky = W)

pavbhaji = Checkbutton(foodFrame, text = 'Pav Bhaji', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var8, command = pavbhaji)
pavbhaji.grid(row = 7, column = 0, sticky = W)

dalbaati = Checkbutton(foodFrame, text = 'Dal-Baati', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var9, command = dalbaati)
dalbaati.grid(row = 8, column = 0, sticky = W)


# Entryfield for Food Items

textroti = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_roti)
textroti.grid(row = 0, column = 1)

textdaal = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_daal)
textdaal.grid(row = 1, column = 1)

textrice = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rice)
textrice.grid(row = 2, column = 1)

textchhole = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_chhole)
textchhole.grid(row = 3, column = 1)

textrajma = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rajma)
textrajma.grid(row = 4, column = 1)

textsahipaneer = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_sahipaneer)
textsahipaneer.grid(row = 5, column = 1)

textdosa = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_dosa)
textdosa.grid(row = 6, column = 1)

textpavbhaji = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_pavbhaji)
textpavbhaji.grid(row = 7, column = 1)

textdalbaati = Entry(foodFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_dalbaati)
textdalbaati.grid(row = 8, column = 1)




# Drinks

lassi = Checkbutton(drinksFrame, text = 'Lassi', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var10, command = lassi)
lassi.grid(row = 0, column = 0, sticky = W)

faluda = Checkbutton(drinksFrame, text = 'Faluda', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var11, command = faluda)
faluda.grid(row = 1, column = 0, sticky = W)

buttermilk = Checkbutton(drinksFrame, text = 'Buttermilk', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var12, command = buttermilk)
buttermilk.grid(row = 2, column = 0, sticky = W)

roohafza = Checkbutton(drinksFrame, text = 'Roohafza', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var13, command = roohafza)
roohafza.grid(row = 3, column = 0, sticky = W)

masalatea = Checkbutton(drinksFrame, text = 'Masala Tea', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var14, command = masalatea)
masalatea.grid(row = 4, column = 0, sticky = W)

coldcoffee = Checkbutton(drinksFrame, text = 'Cold Coffee', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var15, command = coldcoffee)
coldcoffee.grid(row = 5, column = 0, sticky = W)

almondmilk = Checkbutton(drinksFrame, text = 'Almond Milk', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var16, command = almondmilk)
almondmilk.grid(row = 6, column = 0, sticky = W)

sugarcanejuice = Checkbutton(drinksFrame, text = 'Sugar-Cane Juice', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var17, command = sugarcanejuice)
sugarcanejuice.grid(row = 7, column = 0, sticky = W)

jaljeera = Checkbutton(drinksFrame, text = 'Jal Jeera', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var18, command = jaljeera)
jaljeera.grid(row = 8, column = 0, sticky = W)


# Entryfield for Drinks

textlassi = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_lassi)
textlassi.grid(row = 0, column = 1)

textfaluda = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_faluda)
textfaluda.grid(row = 1, column = 1)

textbuttermilk = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_buttermilk)
textbuttermilk.grid(row = 2, column = 1)

textroohafza = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_roohafza)
textroohafza.grid(row = 3, column = 1)

textmasalatea = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_masalatea)
textmasalatea.grid(row = 4, column = 1)

textcoldcoffee = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_coldcoffee)
textcoldcoffee.grid(row = 5, column = 1)

textalmondmilk = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_almondmilk)
textalmondmilk.grid(row = 6, column = 1)

textsugarcanejuice = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_sugarcanejuice)
textsugarcanejuice.grid(row = 7, column = 1)

textjaljeera = Entry(drinksFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_jaljeera)
textjaljeera.grid(row = 8, column = 1)




# Dessert

gulabjamun = Checkbutton(dessertFrame, text = 'Gulabjamun', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var19, command = gulabjamun)
gulabjamun.grid(row = 0, column = 0, sticky = W)

carrothalva = Checkbutton(dessertFrame, text = 'Carrot Halva', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var20, command = carrothalva)
carrothalva.grid(row = 1, column = 0, sticky = W)

jalebi = Checkbutton(dessertFrame, text = 'Jalebi', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var21, command = jalebi)
jalebi.grid(row = 2, column = 0, sticky = W)

rasgulla = Checkbutton(dessertFrame, text = 'Rasgulla', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var22, command = rasgulla)
rasgulla.grid(row = 3, column = 0, sticky = W)

rasmalai = Checkbutton(dessertFrame, text = 'Rasmalai', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var23, command = rasmalai)
rasmalai.grid(row = 4, column = 0, sticky = W)

rabdi = Checkbutton(dessertFrame, text = 'Rabdi', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var24, command = rabdi)
rabdi.grid(row = 5, column = 0, sticky = W)

shrikhand = Checkbutton(dessertFrame, text = 'Shrikhand', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var25, command = shrikhand)
shrikhand.grid(row = 6, column = 0, sticky = W)

barfi = Checkbutton(dessertFrame, text = 'Barfi', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var26, command = barfi)
barfi.grid(row = 7, column = 0, sticky = W)

kheer = Checkbutton(dessertFrame, text = 'Kheer', font = ('ariel', 18, 'bold'), onvalue = 1, offvalue = 0, variable = var27, command = kheer)
kheer.grid(row = 8, column = 0, sticky = W)


# Entryfield for Dessert

textgulabjamun = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_gulabjamun)
textgulabjamun.grid(row = 0, column = 1)

textcarrothalva = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_carrothalva)
textcarrothalva.grid(row = 1, column = 1)

textjalebi = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_jalebi)
textjalebi.grid(row = 2, column = 1)

textrasgulla = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rasgulla)
textrasgulla.grid(row = 3, column = 1)

textrasmalai = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rasmalai)
textrasmalai.grid(row = 4, column = 1)

textrabdi = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rabdi)
textrabdi.grid(row = 5, column = 1)

textshrikhand = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_shrikhand)
textshrikhand.grid(row = 6, column = 1)

textbarfi = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_barfi)
textbarfi.grid(row = 7, column = 1)

textkheer = Entry(dessertFrame, font = ('ariel', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_kheer)
textkheer.grid(row = 8, column = 1)



# Cost & Entryfield

labelCostofFood = Label(costFrame, text = 'Cost of Food', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg = 'white')
labelCostofFood.grid(row = 0, column = 0)

textCostofFood = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = costoffoodvar)
textCostofFood.grid(row = 0, column = 1, padx = 41)


labelCostofDrinks = Label(costFrame, text = 'Cost of Drinks', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg = 'white')
labelCostofDrinks.grid(row = 1, column = 0)

textCostofDrinks = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = costofdrinksvar)
textCostofDrinks.grid(row = 1, column = 1, padx = 41)


labelCostofDesserts = Label(costFrame, text = 'Cost of Desserts', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg = 'white')
labelCostofDesserts.grid(row = 2, column = 0)

textCostofDesserts = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = costofdessertvar)
textCostofDesserts.grid(row = 2, column = 1, padx = 41)


labelSubTotal = Label(costFrame, text = 'Sub Total', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg = 'white')
labelSubTotal.grid(row = 0, column = 2)

textSubTotal = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = subtotalvar)
textSubTotal.grid(row = 0, column = 3, padx = 41)


labelServiceTax = Label(costFrame, text = 'Service Tax', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg ='white')
labelServiceTax.grid(row = 1, column = 2)

textServiceTax = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = servicetaxvar)
textServiceTax.grid(row = 1, column = 3, padx = 41)


labelTotalCost = Label(costFrame, text = 'Total Cost', font = ('arial', 16, 'bold'), bg = 'firebrick4', fg = 'white')
labelTotalCost.grid(row = 2, column = 2)

textTotalCost = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 14, state = 'readonly', textvariable = totalcostvar)
textTotalCost.grid(row = 2, column = 3, padx = 41)



# Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,command=save)
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,command=reset)
buttonReset.grid(row=0,column=4)



# Textarea for Receipt

textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=40,height=14)
textReceipt.grid(row=0,column=0)



#Calculator

operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''    



calculatorField = Entry(calculatorFrame, font = ('arial', 16, 'bold'), width = 30, bd = 2)
calculatorField.grid(row = 0, column = 0, columnspan = 4)


button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=5,width=5,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=5,width=5,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)


button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=5,width=5,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=5,width=5,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)


button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=5,width=5,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=5,width=5,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMulti=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMulti.grid(row=3,column=3)


buttonAns=Button(calculatorFrame,text='Answer',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=5,width=5,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=5,width=5,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttondiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttondiv.grid(row=4,column=3)


root.mainloop()