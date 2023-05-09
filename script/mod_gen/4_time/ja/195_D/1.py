def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0
        for i in range(N):
            for j in range(len(box)):
                if W[i] <= box[j]:
                    ans += V[i]
                    box.pop(j)
                    break
        print(ans)

if __name__ == '__main__':
    main()