import cv2
import sys

def openImage(filename):
    img = cv2.imread(filename)
    if img is None:
        print("Could not open or find the image.")
        sys.exit(1)
    
    # Caso a imagem já não esteja em um tom monocromático agora ela se torna mono
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return image

def display_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def write_image(image, outputFilename):
    cv2.imwrite(outputFilename, image)
