def main():
    import sys
    from math import ceil
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    N = int(readline())
    A = int(readline())
    B = int(readline())
    C = int(readline())
    D = int(readline())
    E = int(readline())
    print(ceil(N/min(A,B,C,D,E))+4)
