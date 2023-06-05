def main():
    # N M Q = map(int, input().split())
    # print(N, M, Q)
    # W = []
    # V = []
    # for i in range(N):
    #     w, v = map(int, input().split())
    #     W.append(w)
    #     V.append(v)
    # print(W)
    # print(V)
    # X = list(map(int, input().split()))
    # print(X)
    # Q = int(input())
    # print(Q)
    # for i in range(Q):
    #     l, r = map(int, input().split())
    #     print(l, r)
    N = 3
    M = 4
    Q = 3
    W = [1, 5, 7]
    V = [9, 3, 8]
    X = [1, 8, 6, 9]
    Q = [[4, 4], [1, 4], [1, 3]]
    for i in range(Q):
        l = Q[i][0]
        r = Q[i][1]
        print(l, r)
        # for j in range(l, r+1):
        #     print(j)
        #     X[j-1] = 0
        # print(X)
        # X.sort()
        # print(X)
        # for j in range(N):
        #     for k in range(M):
        #         if W[j] <= X[k]:
        #             X[k] = 0
        #             break
        # print(X)
        # for j in range(M):
        #     if X[j] != 0:
        #         print(X[j])
        #         X[j] = 0
        #         break
        # print(X)
        # X.sort()
        # print(X)
        # for j in range(N):
        #     for k in range(M):
        #         if W[j] <= X[k]:
        #             X[k] = 0
        #             break
        # print(X)
        # for j in range(M):
        #     if X[j] != 0:
        #         print(X[j])
        #         X[j] = 0
        #         break
        # print(X)
        # X.sort()
        # print(X)

if __name__ == '__main__':
    main()