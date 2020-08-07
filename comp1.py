import numpy as np
import random

def make_sentence(length):
    sentence=""
    a0=np.random.randint(0,10)
    sentence+=str(a0)
    for i in range(length):
        pr=np.random.randint(0,2)
        if a0==0:
            a1=1
        elif a0==9:
            a1=8
        else:
            if pr==0:
                a1=a0-1
            else:
                a1=a0+1
        sentence+=str(a1)
        a0=a1
    return sentence

if __name__ == '__main__':
    l=make_sentence(1000)
    print(l)
