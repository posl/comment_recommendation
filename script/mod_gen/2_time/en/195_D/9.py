def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    X = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    for i in range(M):
        x = int(input())
        X.append(x)
    for i in range(Q):
        l, r = map(int, input().split())
        w = W
        v = V
        x = X
        w = w[l-1:r]
        v = v[l-1:r]
        x = x[l-1:r]
        print(w)
        print(v)
        print(x)

if __name__ == '__main__':
    main()