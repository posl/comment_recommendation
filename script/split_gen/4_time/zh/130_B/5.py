def solution():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0 for i in range(N+1)]
    D[0] = 0
    for i in range(1,N+1):
        D[i] = D[i-1]+L[i-1]
    for i in range(N+1):
        if D[i] > X:
            print(i)
            break
    else:
        print(N+1)
