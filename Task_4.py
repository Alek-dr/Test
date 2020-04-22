import numpy as np
import matplotlib.pyplot as plt

"""
Класс, вычисляющий функцию Гаусса.
Реализовать саму функцию, ее строковое представление,
вывести график на любом интервале x с любыми параметрам функции
"""


class Gauss:

    def __init__(self, mean, std, var):
        self.mean = mean
        self.std = std
        self.var = var

    def prob(self, x):
        """
        :param x: numeric
        :return: value of probability density function
        """
        pass

    def __repr__(self):
        pass

    def plot(self, x: np.array):
        pass


if __name__ == '__main__':
    g = Gauss()
    print(g)
    x = np.arange()
    g.plot(x)
