import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#implement the default mpl key bindings
from scipy.integrate import quad
from matplotlib.backend_bases import key_press_handler
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter import*
import sys

from tkinter import *
import tkinter.font as font
from tkinter import messagebox as msg
import tkinter as tk
from tkinter import ttk

class mclass:
            
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,highlightbackground="black", highlightthickness=2, width=100, height=100, bd= 5)
        self.fr2 = Frame(window,highlightbackground="black", highlightthickness=2, width=100, height=100, bd= 5)
        #ComboBox
        self.num = tk.StringVar()
        self.c = ttk.Combobox(self.fr1, width=40, textvariable=self.num )
        self.c['values'] = (' Méthode des rectangles',' Point Milieux',' Méthode de simpson',' Methode des trapèzes')
        self.c.current(0)
        self.c.grid(row=0,column=1)

        self.bb_txt=StringVar()
        self.bb_txt.set("Le nom de la methode :")
        self.label_bb=Label(self.fr1, textvariable=self.bb_txt,justify=RIGHT, height=4)
        self.label_bb.grid(row=0,column=0)

        self.func_txt=StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4)
        self.label_func.grid(row=1,column=0)

        self.func_txt=StringVar()
        #self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4)
        self.label_func.grid(row=10,column=0)

        self.aa_txt=StringVar()
       # self.func_txt.set("L'expression de f :")
        self.label_aa=Label(self.fr1, textvariable=self.aa_txt,justify=RIGHT, height=4)
        self.label_aa.grid(row=11,column=0)

        self.cc_txt=StringVar()
       # self.func_txt.set("L'expression de f :")
        self.label_cc=Label(self.fr1, textvariable=self.cc_txt,justify=RIGHT, height=4)
        self.label_cc.grid(row=12,column=0)

        self.a_txt=StringVar()
        self.a_txt.set("a:")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4)
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3)
        self.boxa.grid(sticky = W,row=2,column=1)
        self.b_txt=StringVar()
        self.b_txt.set("b:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4)
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3)
        self.boxb.grid(sticky = W,row=3,column=1)
        self.box = Entry(self.fr1,borderwidth=3)
        self.box.grid(row=1,column=1)
        self.n_txt=StringVar()
        self.n_txt.set("Number of points :")
        self.label_n=Label(self.fr1, textvariable=self.n_txt,justify=RIGHT,anchor="w", height=4)
        self.label_n.grid(sticky = E,row=4,column=0)
        self.boxn = Entry(self.fr1,width=10,borderwidth=3)
        self.boxn.grid(sticky = W,row=4,column=1)
        self.box = Entry(self.fr1,borderwidth=3)
        self.box.grid(row=1,column=1)
        

        self.button = Button (self.fr1, width =26,text="Plot",bg="pink", command=self.plot)
        self.button.grid(row=5,column=0,columnspan=3)
        self.button = Button (self.fr1, width =26,text="Effacer",bg="pink", command=self.effacer)
        self.button.grid(row=7,column=0,columnspan=3)
        self.button = Button (self.fr1, width =30,text="Quitter",bg="gray", command=self.quit)
        self.button.grid(row=20,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("gray")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()



    def effacer (self):
        self.c.delete(ALL)
        
    
    
    def quit(self): 
    
        window.quit()
        window.destroy()
    
    
  

    def plot (self):
        self.f= lambda x: eval(self.box.get())
      
        self.a.grid(True)
        test = self.c.get()
        print(test)
        if test == ' Methode des trapèzes':
            
               
            self.TGraph(self.f)
           
        elif test == ' Point Milieux':

            self.MGraph(self.f)
        elif test == ' Méthode des rectangles':
            self.RGraph(self.f)
        elif test == ' Méthode de simpson':
            
            self.SGraph(self.f)
           
           


        else:
            self.aa_txt.set("verifier le nom de la methode ")
            self.func_txt.set("verifier le nom de la methode ")
            self.cc_txt.set("verifier le nom de la methode ")
           




       

       
        
    def TGraph(self,f,resolution=1001):
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            self.a.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        
        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        e=h * s
        self.func_txt.set("Integral Trapèze   = %12.4f" % e)

        I,r =quad(f,int(self.boxa.get()),int(self.boxb.get()))
        self.aa_txt.set("Integral Exacte    = %12.4f" % (I))
        er=I-e
        self.cc_txt.set("Erreur trapeze     = %12.4f" % (er))
        
        
        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(xl, yl,"cs")#point support
        self.a.set_title('Methode des trapèzes')
        self.a.set_ylabel ( ' f ( x ) ' )
        self.canvas.draw()

    

    def MGraph(self,f,resolution=1001):        
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):
            self.m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , f(self.m), f(self.m)  , 0     , 0   ] # ord # ordonnees des sommets
            self.a.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)

        x=self.x# contiens les xi
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        e= h*s
        self.func_txt.set("Integral Milieu   = %12.4f" % e)

        I,r =quad(f,int(self.boxa.get()),int(self.boxb.get()))
        self.aa_txt.set("Integral Exacte    = %12.4f" % (I))
        er=I-e
        self.cc_txt.set("Erreur milieu     = %12.4f" % (er))


        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(self.m,f(self.m),"y*")
        #self.a.plot(xl, yl,"cs")#point support
        self.a.set_title('Methode des milieu')
        self.a.set_ylabel ( ' f ( x ) ' )
        self.a.set_xlabel ( ' x ' )

        self.canvas.draw()


   
    def RGraph(self,f,resolution=1001):
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] # ordonnees des sommets
            self.a.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)

        x=self.x# contiens les xi
        y=f(x)#les yi 
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        e= h * s
        self.func_txt.set("Integral rectangle   = %12.4f" % e)

        
        
        I,r =quad(f,int(self.boxa.get()),int(self.boxb.get()))
        self.aa_txt.set("Integral Exacte    = %12.4f" % (I))
        er=I-e
        self.cc_txt.set("Erreur Rectangle     = %12.4f" % (er))






        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(xl, yl,"rd")#point support
        self.a.set_title('Methode des rectangle')
        self.a.set_ylabel ( ' f ( x ) ' )
        self.a.set_xlabel ( ' x ' )
        self.canvas.draw()


    def SGraph(self,f,resolution=1001):
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):#range intervalle 0 à n
            xx=np.linspace(self.x[i], self.x[i+1], resolution)
            #pour chaque subdivisuion  on doit dessiner polynome dnc on doit aussi le subdiviser
            m=(xl[i]+xl[i+1])/2#pt milieu
            a=xl[i]#borne gauche
            b=xl[i+1]#borne droite
            l0 = (xx-m)/(a-m)*(xx-b)/(a-b)
            l1 = (xx-a)/(m-a)*(xx-b)/(m-b)
            l2 = (xx-a)/(b-a)*(xx-m)/(b-m)
            P = f(a)*l0 + f(m)*l1 + f(b)*l2#fnees des sommets
            self.a.plot(xx, P,"m")
        yflist_fine = f(xlist_fine)

        x=self.x #les points supports xi #x(0)=a-->x(n)=b
        y=f(x) #yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])#pas h=(b-a)/2*n
        n = len(x) - 1#nombre subdivision
        if n % 2 == 1:#si le reste de la division =1 impaire
            n -= 1#☺nombre de sub ywali paire
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
       
        e= h * s / 3.0
        self.func_txt.set("Integral simpson   = %12.4f" % e)

        I,r =quad(f,int(self.boxa.get()),int(self.boxb.get()))
        self.aa_txt.set("Integral Exacte    = %12.4f" % (I))
        er=I-e
        self.cc_txt.set("Erreur simpson     = %12.4f" % (er))



        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(xl, yl,"wp")#point support
        self.a.set_title('Methode des simpson')
        self.a.set_ylabel ( ' f ( x ) ' )
        self.a.set_xlabel ( ' x ' )

        self.canvas.draw()

    
if __name__ == '__main__':
   
  #if __name__ == '__main__':
    window= Tk()

    start= mclass(window)

    window.mainloop()
  
