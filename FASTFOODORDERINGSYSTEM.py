from tkinter import *
from tkinter import ttk
import random
import time
import datetime

root=Tk()
root.geometry("1350x650+0+0")
root.title("foody order sysytem")
root.configure(background="black")
def Exit():
    qExit=messagebox.askyesno("ordering system","Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
   
    CostofDelivery.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeOfOrder.set("")
    DateOfOrder.set("")
def OrderRef():
    Refpay=random.randint(10500,709467)
    Refpaid=("MC"+str(Refpay))
    CustomerRef.set(Refpaid)
def CostofOrder():
    Qty1=float(QtyBurger.get())
    Qty2=float(QtyPizza.get())
    Qty3=float(QtyCoke.get())

    UnitPrice1=float(UnitPriceBurger.get())
    UnitPrice2=float(UnitPricePizza.get())
    UnitPrice3=float(UnitPriceCoke.get())

    CostofWine1="$",str("%.2f"%(Qty1*UnitPrice1))
    CostofWine2="$",str("%.2f"%(Qty2*UnitPrice2))
    CostofWine3="$",str("%.2f"%(Qty3*UnitPrice3))

    CostofBurger.set(CostofWine1)
    CostofPizza.set(CostofWine2)
    CostofCoke.set(CostofWine3)

    CostWine1=(Qty1*UnitPrice1)
    CostWine2=(Qty2*UnitPrice2)
    CostWine3=(Qty3*UnitPrice3)

    AllCost=((Qty1*UnitPrice1)+(Qty2*UnitPrice2)+(Qty3*UnitPrice3))
    TaxAll="$",str("%.2f"%((AllCost)*0.02))
    Tax.set(TaxAll)
    SubTotalp="$",str("%.2f"%(AllCost))
    SubTotal.set(SubTotalp)
    TotalCostp="$",str("%.2f"%(AllCost+((AllCost)*0.02)))
    TotalCost.set(TotalCostp)
    return

#======================Variable===================================

CustomerRef=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofBurger=StringVar()
CostofPizza=StringVar()
CostofCoke=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
CostofBurger=StringVar()
CostofPizza=StringVar()
CostofCoke=StringVar()
UnitPriceCoke=StringVar()
UnitPricePizza=StringVar()
UnitPriceBurger=StringVar()
QtyCoke=StringVar()
QtyPizza=StringVar()
QtyBurger=StringVar()
#Discount=StringVar()
#===============================init component========================================

CostofBurger.set(0)
CostofPizza.set(0)
CostofCoke.set(0)    
CostofBurger.set(0)
CostofPizza.set(0)
CostofCoke.set(0)
UnitPriceCoke.set(0)
UnitPricePizza.set(0)
UnitPriceBurger.set(0)
QtyCoke.set(0)
QtyPizza.set(0)
QtyBurger.set(0)
#Discount.set(0)

TimeOfOrder.set(time.strftime("%H:%M:%S"))# Time
DateOfOrder.set(time.strftime("%d/%m/%y"))# Date
#==============================Frames==================================
Tops=Frame(root,width=1350,height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
LF=Frame(root,width=700,height=650,bd=16,relief="raise")
LF.pack(side=LEFT)
RF=Frame(root,width=600,height=650,bd=16,relief="raise")
RF.pack(side=RIGHT)
Tops.configure(background="black")
LF.configure(background="black")
RF.configure(background="black")
LeftInsideLF=Frame(LF, width=700 ,height=100,bd=8,relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700 ,height=400,bd=8,relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=604 ,height=200,bd=8,relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306 ,height=400,bd=8,relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300 ,height=400,bd=8,relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#===========================ProjectTitle================================
lblInfo=Label(Tops,font=("arial",50,'bold'),text="     Fast Food Ordering System         ",bd=11,anchor='w')
lblInfo.grid(row=0,column=0)
#===============================Top Left Frame====================
lblCustomerName=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Name",
                     fg="black",bd=10,anchor="w")
lblCustomerName.grid(row=0,column=0)
txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=47,
                  bg="lightblue",justify="left",textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerPhone=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Phone",
                     fg="black",bd=10,anchor="w")
lblCustomerPhone.grid(row=1,column=0)
txtCustomerPhone=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=47,
                  bg="lightblue",justify="left",textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lblCustomerEmail=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Email",
                     fg="black",bd=10,anchor="w")
lblCustomerEmail.grid(row=2,column=0)
txtCustomerEmail=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=47,
                  bg="lightblue",justify="left",textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)





#===============================Top Right Frame===================
lblDateofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Date of order",
                     fg="black",bd=10,anchor="w")
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=30,
                  bg="lightblue",justify="left",textvariable=DateOfOrder)
txtDateofOrder.grid(row=0,column=1)

lblTimeofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Time of order",
                     fg="black",bd=10,anchor="w")
lblTimeofOrder.grid(row=1,column=0)
txtTimeofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=30,
                  bg="lightblue",justify="left",textvariable=TimeOfOrder)
txtTimeofOrder.grid(row=1,column=1)

lblCustomerRef=Label(RightInsideLF,font=('arial',12,'bold'),text="Customer Ref",
                     fg="black",bd=10,anchor="w")
lblCustomerRef.grid(row=2,column=0)
txtCustomerRef=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=30,
                  bg="lightblue",justify="left",textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)

#=================================Bottom Right Frame========================
lblMethodOfPayment=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Methoad of Payment',
                          fg="black",bd=16,anchor="w")
lblMethodOfPayment.grid(row=0,column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=('','Cash','Debit Card','Visa Card','Master Card')
cmdMethodOfPayment.grid(row=0,column=1)
#lblDiscount=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Discount',
 #                 fg='black',bd=16,anchor='w')
#lblDiscount.grid(row=1,column=0)
#txtDiscount=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  #bg="blue",justify="left",textvariable=Discount)
#txtDiscount.grid(row=1,column=1)
lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Tax",
             fg="black",bd=16,anchor='w')
lblTax.grid(row=1,column=0)
txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=15,
             bg="lightblue",justify='left',textvariable=Tax)
txtTax.grid(row=1,column=1)
lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Sub Total ",
                  fg="black",bd=16,anchor="w")
lblSubTotal.grid(row=2,column=0)
txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=15,
                  bg="lightblue",justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=2,column=1)

lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Total Cost",
             fg="black",bd=16,anchor='w')
lblTotalCost.grid(row=3,column=0)
txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=15,
                  bg="lightblue",justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=3,column=1)

#========================buttons Left Frame=========================
lblItemOrder=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Item Order',fg="black",bd=20)
lblItemOrder.grid(row=0,column=0)
lblQty=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Quantity',fg="black",bd=10)
lblQty.grid(row=0,column=1)
lblUnitPrice=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Unit Price',fg="black",bd=20)
lblUnitPrice.grid(row=0,column=2)
lblCostofItem=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Cost of Item',fg="black",bd=20)
lblCostofItem.grid(row=0,column=3)
#============
lblBurger=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Burger',fg="black",bd=20)
lblBurger.grid(row=1,column=0)
lblPizza=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Pizza',fg="black",bd=20)
lblPizza.grid(row=2,column=0)
lblCoke=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Coke',fg="black",bd=20)
lblCoke.grid(row=3,column=0)
#==============
txtQtyBurger=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=17,
                  bg="lightblue",justify='left',textvariable=QtyBurger)
txtQtyBurger.grid(row=1,column=1)
txtQtyPizza=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=QtyPizza)
txtQtyPizza.grid(row=2,column=1)
txtQtyCoke=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=QtyCoke)
txtQtyCoke.grid(row=3,column=1)
#======================
txtUnitPriceBurger=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=UnitPriceBurger)
txtUnitPriceBurger.grid(row=1,column=2)
txtUnitPricePizza=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=UnitPricePizza)
txtUnitPricePizza.grid(row=2,column=2)

txtUnitPriceCoke=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=UnitPriceCoke)
txtUnitPriceCoke.grid(row=3,column=2)
#=======================================================================
txtCostofBurger=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=CostofBurger)
txtCostofBurger.grid(row=1,column=3)
txtCostofPizza=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=CostofPizza)
txtCostofPizza.grid(row=2,column=3)
txtCostofCoke=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="lightblue",justify='left',textvariable=CostofCoke)
txtCostofCoke.grid(row=3,column=3)
#==============================Buttons Right Frame------------------
btnDiscount=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',8,'bold'),width=11,
                    text="Discount",bg='lightblue',command=CostofOrder).grid(row=0,column=0)

btnTotalCost=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',8,'bold'),width=11,
                    text="TotalCost",bg='lightblue',command=CostofOrder).grid(row=0,column=0)

btnReset=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',8,'bold'),width=11,
                    text="Reset",bg='lightblue',command=Reset).grid(row=1,column=0)
btnOderRef=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',8,'bold'),width=11,
                    text="OderRef",bg='lightblue',command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',8,'bold'),width=11,
               text="Exit",bg='lightblue',command=Exit).grid(row=3,column=0)
root.mainloop()
