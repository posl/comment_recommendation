def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n,q = map(int,readline().split())
    L = []
    A = []
    for i in range(n):
        l,*a = map(int,readline().split())
        L.append(l)
        A.append(a)
    for i in range(q):
        s,t = map(int,readline().split())
        print(A[s-1][t-1])

if __name__ == '__main__':
    main()