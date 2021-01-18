import tkinter
from tkinter.filedialog import *
import main
import cv2 as cv
from PIL import Image, ImageTk
import PIL
import matplotlib.pyplot as plt
import numpy as np

maFenetre = tkinter.Tk()
maFenetre.title("Traitement des images")
maFenetre.geometry("1200x1000")

f_titre= tkinter.Frame(maFenetre, borderwidth=2, relief=GROOVE)
f_titre.pack(side=TOP,padx=1,pady=30)
Label(f_titre,text="TRAITEMENT DES IMAGES",font=f_titre).pack(padx=0,pady=0)



def seuillageTraitement(seuil, lablResult, path1):
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(seuil, imgGray)
    cv.imwrite('result.png', imgSeuil)
    image = Image.open('result.png').resize((300,300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)


def seuillage(lablResult, path1):
    demandeSeuil = tkinter.Tk()
    demandeSeuil.geometry("200x200")
    slider = Scale(demandeSeuil, from_=0, to=255, orient=HORIZONTAL)
    slider.place(x=50, y=50)
    btn_val = tkinter.Button(demandeSeuil, relief=RAISED, bg="#048b9a", fg="WHITE",text="OK",command=lambda :seuillageTraitement(slider.get(), lablResult, path1))
    btn_val.place(x=75, y=150, width=50, height=20)


def erosion(lablResult, path1):
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgErode = main.erosion(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgErode)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def dilatation(lablResult, path1):
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgDilatation = main.dilatation(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgDilatation)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def ouverture(lablResult, path1):
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgOuverture = main.ouverture(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgOuverture)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def fermeture(lablResult, path1):
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgFermeture = main.fermeture(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgFermeture)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def addition(lablResult, path1, path2):
    img1 = cv.imread(path1)
    img2 = cv.imread(path2)
    imGray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    imgGray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)


    imgAdd = main.addition(imGray1,imgGray2)
    cv.imwrite('result.png', imgAdd)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def soustraction(lablResult, path1, path2):
    img1 = cv.imread(path1)
    img2 = cv.imread(path2)
    imGray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    imgGray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)


    imgAdd = main.soustraction(imGray1,imgGray2)
    cv.imwrite('result.png', imgAdd)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def amincissement(lablResult, path1):
    elementStructurant = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 2]])
    #elementStructurant = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 2]])
    #elementStructurant = np.array([[0, 0, 0], [2, 1, 2], [1, 1, 1]])

    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgAmin = main.amincissement(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgAmin)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def epaississement(lablResult, path1):
    elementStructurant = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 2]])
    #elementStructurant = np.array([[0, 0, 0], [0, 1, 0], [0, 2, 2]])
    #elementStructurant = np.array([[0, 0, 0], [2, 1, 2], [1, 1, 1]])

    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgAmin = main.epaississement(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgAmin)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

def squelettisation(lablResult, path1, nb):
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)
    imgSquel = main.squeletisationLantuejoul(imgSeuil, elementStructurant, nb)
    cv.imwrite('result.png', imgSquel)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)


def nbIteration(lablResult, path1):
    demandeIteration = tkinter.Tk()
    demandeIteration.geometry("200x200")
    slider = Scale(demandeIteration, from_=0, to=50, orient=HORIZONTAL)
    slider.place(x=50, y=50)
    btn_val = tkinter.Button(demandeIteration, relief=RAISED, bg="#048b9a", fg="WHITE",text="OK",command=lambda :squelettisation(lablResult, path1, slider.get()))
    btn_val.place(x=75, y=150, width=50, height=20)

def squelettisation2(lablResult, path1):
    elementStructurant = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 2]])
    elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    img = cv.imread(path1)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgSeuil = main.seuillage(120, imgGray)

    imgSquel2 = main.squelettisationParAmincissement(imgSeuil, elementStructurant)
    cv.imwrite('result.png', imgSquel2)
    image = Image.open('result.png').resize((300, 300))
    image = ImageTk.PhotoImage(image)
    lablResult.config(image=image)
    lablResult.image = image
    lablResult.place(x=0, y=0)

f_image1 = tkinter.Frame(maFenetre,width=300, height=300, bg="white")
f_image2 = tkinter.Frame(maFenetre,width=300, height=300, bg="white")
f_image_result = tkinter.Frame(maFenetre,width=300, height=300, bg="white")

####################BOUTONS
btn = tkinter.Frame(maFenetre,width=250, height=1000, bd=10)

labl = tkinter.Label(f_image1)
labl2 = tkinter.Label(f_image2)
lablResult = tkinter.Label(f_image_result)


    #boutons traitement
btn_seuillage=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SEUILLAGE",command=lambda: seuillage(lablResult, path1))
btn_erosion=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="ESROSION",command=lambda: erosion(lablResult, path1))
btn_dilatation=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="DILATATION",command=lambda: dilatation(lablResult, path1))
btn_ouverture=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="OUVERTURE",command=lambda: ouverture(lablResult, path1))
btn_fermeture=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="FERMETURE",command=lambda: fermeture(lablResult, path1))
btn_addition=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="ADDITION",command=lambda: addition(lablResult,path1,path2))
btn_soustraction=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SOUSTRATION",command=lambda: soustraction(lablResult,path1,path2))
btn_amincissement=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="AMINCISSEMENT",command=lambda: amincissement(lablResult,path1))
btn_epaississement=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="EPAISSISSEMENT",command=lambda: epaississement(lablResult,path1))
btn_squelletisation=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SQUELETTISATION\nLANTUEJOUL",command=lambda: nbIteration(lablResult,path1))
btn_squelletisation2=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SQUELETTISATION\nAMINCISSEMENT",command=lambda: squelettisation2(lablResult,path1))


    #boutons charges image
def charge(labl):
    filepathCharge = askopenfilename(initialdir="/", title="Open as", defaultextension="*.*", filetypes=(("JPG files", "*.jpg"),("PNG files", "*.png"), ("all files", "*.*")))
    image = Image.open(filepathCharge).resize((300,300))
    global path1
    path1= filepathCharge
    image = ImageTk.PhotoImage(image)
    labl.config(image=image)
    labl.image = image
    labl.place(x=0, y=0)

def charge2(labl):
    filepathCharge = askopenfilename(initialdir="/", title="Open as", defaultextension="*.*",
                                     filetypes=(("JPG files", "*.jpg"),("PNG files", "*.png"), ("all files", "*.*")))
    image = Image.open(filepathCharge).resize((300, 300))
    global path2
    path2 = filepathCharge
    image = ImageTk.PhotoImage(image)
    labl.config(image=image)
    labl.image = image
    labl.place(x=0, y=0)

    #ajout des boutons
btn_seuillage.place(x=0, y=0, height=30, width=150)
btn_erosion.place(x=0, y=50, height=30, width=150)
btn_dilatation.place(x=0, y=100, height=30, width=150)
btn_ouverture.place(x=0, y=150, height=30, width=150)
btn_fermeture.place(x=0, y=200, height=30, width=150)
btn_addition.place(x=0, y=250, height=30, width=150)
btn_soustraction.place(x=0, y=300, height=30, width=150)
btn_amincissement.place(x=0, y=350, height=30, width=150)
btn_epaississement.place(x=0, y=400, height=30, width=150)
btn_squelletisation.place(x=0, y=450, height=35, width=150)
btn_squelletisation2.place(x=0, y=505, height=35, width=150)

bt_Charge = tkinter.Button(maFenetre, relief=RAISED, bg="#048b9a", fg="WHITE",
                           text="OUVRIR UNE IMAGE",
                           command=lambda: charge(labl))
bt_Charge.place(x=375, y=400, height=30, width=150)

bt_Charge2 = tkinter.Button(maFenetre, relief=RAISED, bg="#048b9a", fg="WHITE",
                           text="OUVRIR UNE IMAGE",
                           command=lambda: charge2(labl2))
bt_Charge2.place(x=700, y=400, height=30, width=150)


btn.place(x=10, y=100)
f_image1.place(x=300, y=75)
f_image2.place(x=625, y=75)
f_image_result.place(x=450, y=450)

maFenetre.mainloop()

