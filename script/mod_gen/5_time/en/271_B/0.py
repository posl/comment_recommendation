def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

if __name__ == '__main__':
    main()