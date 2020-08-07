import numpy as np
from comp1 import make_sentence
from collections import Counter
import time, sys, getopt, os.path
from bitio import *

MIN_LEN = 3
MAX_LEN = 18
LEN_BITS = 4
POS_BITS = 13

class Slide:
    def __init__(self, file):
        self.file = file
        self.size = 1 << POS_BITS
        self.limit = self.size * 2
        self.next = [None] * self.size
        self.ht = {}
        self.buff = [0] * (self.limit + MAX_LEN)
        self.data_size = self.fread(0, self.limit + MAX_LEN)
        self.match_len = 0
        self.match_pos = 0
    # ハッシュ値を求める
    def hash_value(self, rp):
        value = 0
        for x in range(MIN_LEN):
            value = (value << 8) + self.buff[rp + x]
        return value
    # データ入力
    def fread(self, start, size):
        for i in range(size):
            c = self.file
            if c is None: return i
            self.buff[start + i] = c
        return size
    # データ移動
    def move_data(self, to, from_, size):
        for n in range(size):
            self.buff[to + n] = self.buff[from_ + n]
    # スライド窓の更新
    def update(self, rp):
        if self.data_size < self.limit + MAX_LEN: return rp
        # buffer update
        self.move_data(0, self.size, self.size + MAX_LEN)
        n = self.fread(self.size + MAX_LEN, self.size)
        self.data_size = self.size + MAX_LEN + n
        # hash update
        for k, v in self.ht.items():
            if v < self.size:
                del self.ht[k]
            else:
                self.ht[k] = v - self.size
        for x in range(self.size):
            v = self.next[x]
            if v == None or v < self.size:
                self.next[x] = None
            else:
                self.next[x] = v - self.size
        return rp - self.size
    # データの挿入
    def insert(self, rp):
        value = self.hash_value(rp)
        if value in self.ht:
            self.next[rp & (self.size - 1)] = self.ht[value]
        else:
            self.next[rp & (self.size - 1)] = None
        self.ht[value] = rp
    # 最長一致列の探索
    def search(self, rp):
        b = self.buff
        value = self.hash_value(rp)
        limit = rp - self.size
        self.match_len = 0
        self.match_pos = 0
        if value in self.ht:
            n = self.ht[value]
            while n is not None and n >= limit:
                if b[rp + self.match_len] == b[n + self.match_len]:
                    x = 0
                    while x < MAX_LEN:
                        if b[rp + x] != b[n + x]: break
                        x += 1
                    if self.match_len < x:
                        self.match_len = x
                        self.match_pos = n
                        if x == MAX_LEN: break
                n = self.next[n & (self.size - 1)]
        # データの終端をチェック
        if self.match_len >= self.data_size - rp:
            self.match_len = self.data_size - rp

def encode(fin, fout):
    s = Slide(fin)
    rp = 0
    while rp < s.data_size:
        s.search(rp)
        if s.match_len < MIN_LEN:
            num = 1
            fout.putbit(0)
            fout.putbits(8, s.buff[rp])
        else:
            num = s.match_len
            fout.putbit(1)
            fout.putbits(LEN_BITS, num - MIN_LEN)
            fout.putbits(POS_BITS, rp - s.match_pos - 1)
        for _ in range(num):
            s.insert(rp)
            rp += 1
            if rp >= s.limit: rp = s.update(rp)

if __name__ == '__main__':
    main()
