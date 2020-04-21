import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import affine_transform


def rgb2gray(img: np.array) -> np.array:
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    return 0.2989 * r + 0.5870 * g + 0.1140 * b


@gray_decor
def transform(img: np.array) -> np.array:
    M = np.array([[0.8, 0.3],
                  [-0.3, 0.8]])
    return affine_transform(img, M)


"""
Задача: код в main выполняет некоторое афинное преобразование,
но только при условии, что изображение черно-белое. Чтобы получить черно-белое изображение, у нас
есть функция rgb2gray. Она нужна так часто, что хочется написать декоратор gray_decor.
TODO: написать декоратор 
"""

if __name__ == '__main__':
    img = plt.imread("data/kazino.png", 0)
    t = transform(img)
    plt.imshow(t, cmap='gray')
    plt.show()
