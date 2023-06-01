Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    for i in range(1, 100):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 3

def solve():
    a,b = map(int, input().split())
    for i in range(1, 1000):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def get_price(A,B):
    for i in range(1,100):
        if int(i*0.08)==A and int(i*0.1)==B:
            return i
    return -1

A,B=map(int,input().split())
print(get_price(A,B))

=======
Suggestion 5

def get_price(A,B):
    for i in range(1,101):
        if int(i*0.08) == A and int(i*0.1) == B:
            return i
    return -1

A,B = map(int,input().split())
print(get_price(A,B))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve(a,b):
    for i in range(1, 100):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 8

def calc_tax(price, tax_rate):
    return int(price * tax_rate)

=======
Suggestion 9

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

import math
import sys
