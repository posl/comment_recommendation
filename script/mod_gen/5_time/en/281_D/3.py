def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        S.add(A[i])
    if len(S) == 0:
        print(-1)
        exit()
    if len(S) == 1:
        if D in S:
            print(D)
        else:
            print(-1)
        exit()
    for i in range(10 ** 9):
        if D * i in S:
            print(D * i)
            exit()
        if D * (i + 1) in S:
            print(D * (i + 1))
            exit()
    print(-1)

if __name__ == '__main__':
    main()