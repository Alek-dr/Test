import matplotlib.pyplot as plt
import numpy as np
from joblib import load


def task1():
    """
    model_1 - сохраненная sklearn модель уравнения регрессии y = x^2 + x + b
    коэффициенты модели сохранены в правильном порядке (x^2, x^1)
    Задача: исследовать модель, написать уравнение (учитывая, что в данных присутствовал шум)
    и построить график на интервале x (задан ниже)
    """
    model = load("data/model_1.clf")
    x = np.array(np.arange(0, 10, 0.1))
    # TODO : график


def task2():
    """
    Используя все ту же модель, проверить коэффициент детерминации R^2
    для этой модели и зависимости ниже
    построить две зависимости на одном графике
    """
    model = load("data/model_1.clf")
    x = np.array(np.arange(0, 10, 0.1))
    y = 3 * x * x - 15 * x - 17


if __name__ == '__main__':
    task1()
