import sys
import re

def check_image_extension(filename):
    return bool(re.search(r'\.(png|jpg|jpeg|gif|bmp)$', filename, re.IGNORECASE))

def main(imageName, reductionPercentage, technique):
    print(f"Parameter 1: {imageName}")
    print(f"Parameter 2: {reductionPercentage}")
    print(f"Parameter 3: {technique}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("You must provide exactly 3 parameters.")
        sys.exit(1)
    
    imageName = sys.argv[1]
    if not check_image_extension(imageName):
        print("You must provide an image.")
        sys.exit(1)
    reductionPercentage = int(sys.argv[2])
    if reductionPercentage <= 0 or reductionPercentage >=100:
        print("You must provide a valid reduction percentage.")
        sys.exit(1)
    technique = sys.argv[3]
    if technique not in ['media','moda','mediana']:
        print("You must provide a valid reduction technique.")
        sys.exit(1)
    
    main(imageName, reductionPercentage, technique)
