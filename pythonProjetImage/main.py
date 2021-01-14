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
                    somme = somme +img[i+k,j-l] * elementStructurant[k+widthElt//2,l+heightElt//2]

            if somme == 1275:
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
                    somme = somme +img[i+k,j-l] * elementStructurant[k+widthElt//2,l+heightElt//2]

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
            pixel = img[i, j] + img2[i, j]

            if pixel>255:
                pixel=255

            imgAddition[i,j]=pixel

    return imgAddition



def soustraction(img, img2):
    print("soustraction")
    imgSoustraction = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j] - img2[i, j]

            if pixel < 0:
                pixel = 0

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

def squeletisationLantuejoul(img,elementStructurant,nbIteration):
    print("Lantuejoul")
    imgAdd=img.copy
    for nb in range(1,nbIteration):
        imgErode=erosion(imgSeuil, nb*elementStructurant)
        imgOuvertureErode=ouverture(imgErode,elementStructurant)
        imgSous=soustraction(imgErode,imgOuvertureErode)
        if nb!=1:
            imgAdd=addition(imgAdd, imgSous)
        else:
            imgAdd=imgSous
    return imgAdd

######################MAIN
img = cv.imread('fruits.jpg')
img2 = cv.imread('fruits2.jpg')
#img = cv.imread('croix.png')
#img2 = cv.imread('croix2.png')
#img = cv.imread('Rect.png')
imgGray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#imgGray2= cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

elementStructurant = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])


imgSeuil = seuillage(120, imgGray)

imgErodee = erosion(imgSeuil, elementStructurant)
#
# imgDilatee = dilatation(imgSeuil, elementStructurant)
#
# imgOuverture = ouverture(imgSeuil, elementStructurant)
#
# imgFermeture = fermeture(imgSeuil, elementStructurant)


#imgAdd = addition(imgGray, imgGray2)
#imgSous = soustraction(imgGray, imgGray2)

# imgL = squeletisationLantuejoul(imgGray,elementStructurant,2)
#
# plt.subplot(3, 3, 1)
# plt.title("Image d'origine")
# plt.imshow(imgGray, cmap='gray')
#
# plt.subplot(3, 3, 2)
# plt.title("Image seuillage")
# plt.imshow(imgSeuil, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 3)
# plt.title("Image érodée")
# plt.imshow(imgErodee, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 4)
# plt.title("Image dilatée")
# plt.imshow(imgDilatee, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 5)
# plt.title("Image ouverture")
# plt.imshow(imgOuverture, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 6)
# plt.title("Image fermeture")
# plt.imshow(imgFermeture, cmap='gray', vmin=0, vmax=1)
#
# plt.subplot(3, 3, 7)
# plt.title("Image addition")
# plt.imshow(imgAdd,cmap='gray')
#
# plt.subplot(3, 3, 8)
# plt.title("Image soustraction")
# plt.imshow(imgSous,cmap='gray')

# plt.subplot(3, 3, 9)
# plt.title("Image Lantuejoul")
# plt.imshow(imgL,cmap='gray')

plt.show()

