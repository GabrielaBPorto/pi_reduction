import sys
from param_utils import param_checking
from image_utils import openImage, write_image, display_image
from sampling_techniques import reduce_sample_by_technique

def main(imageName, reductionPercentage, technique):
    img = openImage(imageName)
    print("Por favor espere enquanto está aplicando a técnica sobre a imagem...")
    reduced = reduce_sample_by_technique(img, reductionPercentage, technique)
    write_image(reduced,f"{imageName.split('.')[0]}_{technique}_{reductionPercentage}.png")
    # display_image(reduced)

if __name__ == "__main__":
    imageName = sys.argv[1]
    reductionPercentage = int(sys.argv[2])/100
    technique = sys.argv[3]
    param_checking(imageName, reductionPercentage, technique)
    main(imageName, reductionPercentage, technique)
