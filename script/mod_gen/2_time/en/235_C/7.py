def main():
    # N, Q = map(int, input().split())
    # A = list(map(int, input().split()))
    # X = []
    # K = []
    # for i in range(Q):
    #     x, k = map(int, input().split())
    #     X.append(x)
    #     K.append(k)
    N, Q = 6, 8
    A = [1, 1, 2, 3, 1, 2]
    X = [1, 1, 1, 1, 2, 2, 2, 4]
    K = [1, 2, 3, 4, 1, 2, 3, 1]
    for i in range(Q):
        x = X[i]
        k = K[i]
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
                if count == k:
                    print(j + 1)
                    break
        else:
            print(-1)

if __name__ == '__main__':
    main()