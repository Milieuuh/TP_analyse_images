import tkinter
from tkinter.filedialog import *
import main
import cv2 as cv
from PIL import ImageTk
import PIL

maFenetre = tkinter.Tk()
maFenetre.title("Traitement des images")
maFenetre.geometry("1200x1000")

f_titre= tkinter.Frame(maFenetre, borderwidth=2, relief=GROOVE)
f_titre.pack(side=TOP,padx=1,pady=30)
Label(f_titre,text="TRAITEMENT DES IMAGES",font=f_titre).pack(padx=10,pady=10)


def seuillage(img, seuil):
    imgSeuil = main.seuillage(seuil, img)

img = cv.imread('fruits.jpg')
imgGray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)


##########################IMAGES
image_f = tkinter.Frame(maFenetre,width=500, height=1000, bd=10)
zone_image = Canvas(image_f, width=400, height=400, bg="white")
zone_image.grid(row=0, column=1)

####################BOUTONS
btn = tkinter.Frame(maFenetre,width=500, height=1000, bd=10)


    #boutons traitement
btn_seuillage=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SEUILLAGE",command=seuillage(imgGray, 120))
btn_erosion=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="ESROSION",command=seuillage(imgGray, 120))
btn_dilatation=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="DILATATION",command=seuillage(imgGray, 120))
btn_ouverture=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="OUVERTURE",command=seuillage(imgGray, 120))
btn_fermeture=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="FERMETURE",command=seuillage(imgGray, 120))
btn_addition=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="ADDITION",command=seuillage(imgGray, 120))
btn_soustraction=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="SOUSTRATION",command=seuillage(imgGray, 120))
btn_amincissement=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="AMINCISSEMENT",command=seuillage(imgGray, 120))
btn_epaississement=tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="EPAISSISSEMENT",command=seuillage(imgGray, 120))

    #boutons charges image


def charge():
    filepathCharge = askopenfilename(initialdir="/", title="Open as", defaultextension="*.*", filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    # image = ImageTk.PhotoImage(file=filepathCharge)
    # zone_image.create_image(100, 100, image=image)


bt_Charge = tkinter.Button(btn, relief=RAISED, bg="#048b9a", fg="WHITE",text="OUVRIR UNE IMAGE",command=charge)


    #ajout des boutons
btn_seuillage.grid(row=0,column=0, ipadx=60, pady=20)
btn_erosion.grid(row=1,column=0, ipadx=60, pady=20)
btn_dilatation.grid(row=2,column=0, ipadx=60, pady=20)
btn_ouverture.grid(row=3,column=0, ipadx=60, pady=20)
btn_fermeture.grid(row=4,column=0, ipadx=60, pady=20)
btn_addition.grid(row=5,column=0, ipadx=60, pady=20)
btn_soustraction.grid(row=6,column=0, ipadx=50, pady=20)
btn_amincissement.grid(row=7,column=0, ipadx=40, pady=20)
btn_epaississement.grid(row=8,column=0, ipadx=40, pady=20)

bt_Charge.grid(row=0,column=1, ipadx=60, padx=500)

btn.pack(side=LEFT)

maFenetre.mainloop()