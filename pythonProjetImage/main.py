import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def seuillage(seuil, img):
    print("seuillage")
    imageSeuil = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > seuil:
                imageSeuil[i, j] = 255
            else:
                imageSeuil[i, j] = 0

    return imageSeuil

def erosion(img, elementStructurant):
    print("erosion")
    imageErosion = img.copy()
    #largeur et longueur de l'élément structurant
    widthElt = elementStructurant.shape[0]
    heightElt = elementStructurant.shape[1]

    for i in range(widthElt//2,img.shape[0]- widthElt//2):
        for j in range(heightElt//2, img.shape[1]-heightElt//2):
            somme = 0
            for k in range(0 - widthElt//2, widthElt - widthElt//2):
                for l in range(0 - heightElt //2, heightElt -heightElt //2):
                    somme = somme + img[i+k,j+l] * elementStructurant[k+widthElt//2,l+heightElt//2]

            if somme >= 1275:
                imageErosion[i,j] = 255
            else:
                imageErosion[i,j] = 0

    return imageErosion



def dilatation(img, elementStructurant):
    print("dilatation")
    imageDilatation = img.copy()

    #largeur et longueur de l'élément structurant
    widthElt = elementStructurant.shape[0]
    heightElt = elementStructurant.shape[1]

    for i in range(widthElt//2,img.shape[0]- widthElt//2):
        for j in range(heightElt//2, img.shape[1]-heightElt//2):
            somme = 0
            for k in range(0 - widthElt//2, widthElt - widthElt//2):
                for l in range(0 - heightElt //2, heightElt -heightElt //2):
                    somme = somme +img[i+k,j+l] * elementStructurant[k+widthElt//2,l+heightElt//2]

            if somme == 0:
                imageDilatation[i,j] = 0
            else:
                imageDilatation[i,j] = 255

    return imageDilatation


def addition(img, img2):
    print("addition")
    imgAddition = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val1 = int(img[i, j])
            val2 = int(img2[i, j])
            pixel = val1 + val2
            if pixel>255:
                imgAddition[i,j]=255
            else:
                imgAddition[i,j]=pixel

    return imgAddition



def soustraction(img, img2):
    print("soustraction")
    imgSoustraction = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val1 = int(img[i, j])
            val2 = int(img2[i, j])
            pixel = val1 - val2
            if pixel < 0:
                imgSoustraction[i, j] = 0
            else:
                imgSoustraction[i, j] = pixel

    return imgSoustraction


def ouverture(img, elementStructurant):
    print("ouverture")
    imgErode = erosion(img, elementStructurant)
    result = dilatation(imgErode, elementStructurant)

    return result


def fermeture(img, elementStructurant):
    print("fermeture")
    imgD = dilatation(img, elementStructurant)
    result = erosion(imgD, elementStructurant)

    return result

def squeletisationLantuejoul(img,elementStructurant2,nbIteration):
    print("Lantuejoul")
    imgAdd=img.copy()

    for nb in range(0,nbIteration):
        imgErode = img.copy()
        for x in range(0, nb):
            imgErode=erosion(imgErode, elementStructurant2)

        imgOuvertureErode=ouverture(imgErode, elementStructurant2)
        imgSous=soustraction(imgErode, imgOuvertureErode)

        if nb>0:
            imgAdd=addition(imgAdd, imgSous)
        else:
            imgAdd=imgSous

        # cv.namedWindow('img', cv.WINDOW_NORMAL)
        # cv.imshow('img', imgAdd)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

    return imgAdd

def amincissement(img, elementStructurant):
    #print("ammincissement")
    imgAmincie = img.copy()

    # largeur et longueur de l'élément structurant
    widthElt = elementStructurant.shape[0]
    heightElt = elementStructurant.shape[1]

    for i in range(widthElt // 2, img.shape[0] - widthElt // 2):
        for j in range(heightElt // 2, img.shape[1] - heightElt // 2):
            bool = True
            for k in range(0 - widthElt // 2, widthElt - widthElt // 2):
                for l in range(0 - heightElt // 2, heightElt - heightElt // 2):
                    var = elementStructurant[k+1, l+1]
                    if(var==1):
                        var =255
                    if img[i+k,j+l]!=var and elementStructurant[k+1,l+1]!=2:
                       bool = False
            if bool == False:
                imgAmincie[i,j]=0
            else:
                imgAmincie[i,j]=255

    return imgAmincie

def epaississement(img, elementStructurant):
    imgEpaississement = img.copy()

    # largeur et longueur de l'élément structurant
    widthElt = elementStructurant.shape[0]
    heightElt = elementStructurant.shape[1]

    for i in range(widthElt // 2, img.shape[0] - widthElt // 2):
        for j in range(heightElt // 2, img.shape[1] - heightElt // 2):
            bool = True
            for k in range(0 - widthElt // 2, widthElt - widthElt // 2):
                for l in range(0 - heightElt // 2, heightElt - heightElt // 2):
                    var = elementStructurant[k+1, l+ 1]
                    if(var ==1):
                        var =255

                    if img[i+k,j+l]==var and elementStructurant[k+1 ,l+1]!=2:
                       bool = False
            if bool == False:
                imgEpaississement[i,j]=255
            else:
                imgEpaississement[i,j]=0

    return imgEpaississement

def differenceImage(img1, img2):
    bool = True
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if img1[i,j] != img2[i,j]:
                bool = False
    return bool


def squelettisationParAmincissement(img, elementStructurant):
    print("Squeletisation par amincissement")
    imgSquelette = img.copy()
    nb=0
    while True:

        imgAvant = imgSquelette
        if nb==0:
            imgSquelette = amincissement(img, elementStructurant)
        else:
            imgSquelette = amincissement(imgSquelette, elementStructurant)
        print(nb)
        nb=nb+1
        if nb==10:#differenceImage(imgSquelette, imgAvant): #nb==30:
            break

    return imgSquelette


######################MAIN
# img = cv.imread('fruits.jpg')
# img2 = cv.imread('fruits2.jpg')
img = cv.imread('croix_new.png')
img2 = cv.imread('croix_new.png')
#img = cv.imread('Rect.png')
imgGray= cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#imgGray2= cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

elementStructurantAE = np.array([[1, 2, 1], [1, 1, 2], [2, 1, 2]])
elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])


imgSeuil = seuillage(120, imgGray)

#imgErodee = erosion(imgSeuil, elementStructurant)
#
# imgDilatee = dilatation(imgSeuil, elementStructurant)
#
imgOuverture = ouverture(imgSeuil, elementStructurant)
#
# imgFermeture = fermeture(imgSeuil, elementStructurant)


#imgAdd = addition(imgOuverture, imgSeuil)
imgSous = soustraction(imgSeuil,imgOuverture)

imgL = squeletisationLantuejoul(imgSeuil,elementStructurant,10)
#imgL = epaississement(imgSeuil,elementStructurantAE)
#imgL = amincissement(imgSeuil,elementStructurantAE)
#imgL = squelettisationParAmincissement(imgSeuil, elementStructurantAE)


#
# plt.subplot(1, 2, 1)
# plt.title("Image d'origine")
# plt.imshow(imgSeuil, cmap='gray')

plt.subplot(3, 3, 2)
plt.title("Image seuillage")
plt.imshow(imgSeuil, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 3)
# plt.title("Image érodée")
# plt.imshow(imgErodee, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 4)
# plt.title("Image dilatée")
# plt.imshow(imgDilatee, cmap='gray', vmin=0, vmax=1)
#
plt.subplot(3, 3, 5)
plt.title("Image ouverture")
plt.imshow(imgOuverture, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 6)
# plt.title("Image fermeture")
# plt.imshow(imgFermeture, cmap='gray', vmin=0, vmax=1)
#
#plt.subplot(3, 3, 6)
#plt.title("Image addition")
#plt.imshow(imgAdd,cmap='gray')
#
plt.subplot(3, 3, 8)
plt.title("Image soustraction")
plt.imshow(imgSous,cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Image Lantuejoul")
plt.imshow(imgL, cmap='gray')

plt.show()

