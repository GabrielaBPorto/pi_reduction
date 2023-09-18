
import numpy as np
import numpy.ma as ma
from scipy import stats


def applyTechnique(block, technique):       
    if technique == 'moda':
        return stats.mode(block, axis=None)[0]
    elif technique == 'media':
        return np.mean(block).astype(np.uint8)
    else:
        return np.median(block).astype(np.uint8)


def reduce_sample_by_technique(image, reduction_factor, technique):
    # Inicialização de todos os dados necessários
    height, width = image.shape
    new_height, new_width = int(height * reduction_factor), int(width * reduction_factor)
    block_size_height = height // new_height
    block_size_width = width // new_width
    reduced_image = np.zeros((new_height, new_width), dtype=np.uint8)

    # Ativamente percorrendo a imagem e aplicando a técnica para cada bloco a partir do fator de redução
    for i in range(new_height):
        for j in range(new_width):
            y_start, y_end = i * block_size_height, (i + 1) * block_size_height
            x_start, x_end = j * block_size_width, (j + 1) * block_size_width
            block = image[y_start:y_end, x_start:x_end]
            value = applyTechnique(block, technique)
            reduced_image[i, j] = value

    return reduced_image
