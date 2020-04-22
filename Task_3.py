import multiprocessing as mp
import random
import string
import numpy as np

""""
Вам достался этот код. Допустим, он имеет смысл.
TODO: отрефакторить
"""

def check_string(s: str) -> None:
    n = 0
    for ch in s:
        if ch == "|":
            continue
        n += ord(ch)
    if n % 2 == 0:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    L = []
    for i in range(10):
        s = ""
        for j in range(np.random.randint(1, 15)):
            s += "|" + random.choice(string.ascii_letters)
        L.append(s)
    processes = []
    for s in L:
        p = mp.Process(target=check_string, args=(s,))
        p.start()
