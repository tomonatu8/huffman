import numpy as np
import random

def make_sentence(length):
    sentence=""
    for i in range(length):
        a0=np.random.randint(0,10)
        sentence+=str(a0)
    return sentence

if __name__ == '__main__':
    l=make_sentence(1000)
    print(l)
    print(len(l))
