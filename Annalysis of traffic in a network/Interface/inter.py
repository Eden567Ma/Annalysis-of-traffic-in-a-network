import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App:
    def __init__(self, master=tk.Tk()):
        self.master = master
        self.master.configure(background="#eb984e")
        self.fig_size = [700, 600]
        self.frame = tk.Frame(master)
        self.frame.configure(background="#eb984e")
        self.canvas = tk.Canvas(self.frame, width=1280, height=800)
        self.canvas.configure(background="white")
        self.canvas.pack()
        self.load_image('visualisation.png')
        self.image_label = tk.Label(self.canvas, image=self.fig_image)
        self.image_label.place(x=315, y=100)
        self.button_left = tk.Button(self.frame, text="TCP",
                                     command=self.update)
        self.button_left.pack(side='right')
        self.button_right = tk.Button(self.frame, text="HTTP",
                                     command=self.update1)
        self.button_right.pack(side='left')
        self.ref = tk.Button(self.frame, text="IP",
                                     command=self.update2)
        self.ref.pack(side='top')
        self.button_menu= tk.Button(self.master, text="Quitter", command=self.master.quit)
        self.button_menu.place(x=930, y=900)
        self.frame.bind("q", self.close)
        self.frame.bind("<Escape>", self.close)
        self.frame.pack()
        self.frame.focus_set()
        self.is_active = True
        
        #self.combo()
    def docs() :
        fent=tk.Tk()
        fent.title(" Infos du projet ")
        fent.geometry("900x900")
        menubar = tk.Menu(fent)
        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Quitter", command=fent.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)
        fent.config(menu=menubar) 
    def load_image(self, filename):
        self.fig_image = ImageTk.PhotoImage(Image.open(filename).resize(self.fig_size, Image.BILINEAR))

    def update(self, *args):
        self.load_image('tcp.png')
        self.image_label.config(image=self.fig_image)

    def update1(self, *args):
        self.load_image('http.png')
        self.image_label.config(image=self.fig_image)

    def update2(self, *args):
        self.load_image('ip.png')
        self.image_label.config(image=self.fig_image)

    def menu(self) :
        menubar = tk.Menu(self.master)
# créer un sous-menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.docs)
        filemenu.add_command(label="Open", command=self.docs)
        filemenu.add_command(label="Save", command=self.docs)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Quit!", command=self.master.quit)
# afficher le menu
    

    def close(self, *args):
        print('GUI closed...')
        self.master.quit()
        self.is_active = False

    def is_closed(self):
        return not self.is_active

    def docs() :
     fent=tk.Tk()
     fent.title(" Infos du projet ")
     fent.geometry("900x900")
     menubar = tk.Menu(fent)
     menu1 = tk.Menu(menubar, tearoff=0)
     menu1.add_command(label="Quitter", command=fent.quit)
     menubar.add_cascade(label="Fichier", menu=menu1)
     fent.config(menu=menubar)
     fent.mainloop()
     
    def propos() :
         infos=tk.Tk()
         infos.title(" Presentation ")
         infos.geometry("600x700")
         tk.Label(infos,text='Ce projet est un Visualisateur de trafic réseau.\n Il a été codé en Python. \n Il permet de générer les flux de trafic qui font référence aux trames échangées dans le cadre d’un protocole \n Exécuté à l’initiative de deux machines.\n').pack()
         tk.Label(infos,text='Ce projet est un Visualisateur de trafic réseau.\n Il a été codé en Python. \n Il permet de générer les flux de trafic qui font référence aux trames échangées dans le cadre d’un protocole \n Exécuté à l’initiative de deux machines.\n').pack()
         quit = tk.Button(infos,text='Quitter', command=infos.quit)
         quit.pack()
    def createNewWindow():
      
      newWindow = tk.Toplevel(app)
      labelExample = tk.Label(newWindow, text = "New Window")
      buttonExample = tk.Button(newWindow, text = "New Window button")

      labelExample.pack()
      buttonExample.pack()

    def mainloop(self):
        self.master.mainloop()
        print('mainloop closed...')

if __name__ == '__main__':
    import time
    app = App()
    app.mainloop()
