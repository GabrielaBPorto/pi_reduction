import sys
import re
import cv2

def check_image_extension(filename):
    return bool(re.search(r'\.(png|jpg|jpeg|gif|bmp)$', filename, re.IGNORECASE))

def openImage(filename):
    img = cv2.imread(filename)
    if img is None:
        print("Could not open or find the image.")
        sys.exit(1)
    return img

def display_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def param_checking(filename,percentage,technique):
    if not check_image_extension(filename):
        print("You must provide an image.")
        sys.exit(1)
    if percentage <= 0 or percentage >=100:
        print("You must provide a valid reduction percentage.")
        sys.exit(1)
    if technique not in ['media','moda','mediana']:
        print("You must provide a valid reduction technique.")
        sys.exit(1)

def main(imageName, reductionPercentage, technique):
    print(f"Parameter 1: {imageName}")
    print(f"Parameter 2: {reductionPercentage}")
    print(f"Parameter 3: {technique}")
    img = openImage(imageName)

    # Caso a imagem já não esteja em um tom monocromático agora ela se torna mono
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display_image(img)
    display_image(image)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("You must provide exactly 3 parameters.")
        sys.exit(1)
    
    imageName = sys.argv[1]
    reductionPercentage = int(sys.argv[2])
    technique = sys.argv[3]
    param_checking(imageName, reductionPercentage, technique)
    main(imageName, reductionPercentage, technique)
