def solution():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(0, N):
        if P[i] == X:
            print(i+1)
solution()
