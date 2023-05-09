def main():
    import sys
    readline = sys.stdin.readline
    A, B, N = map(int, readline().split())
    if N < B:
        print((A*N)//B)
    else:
        print((A*(B-1))//B)
