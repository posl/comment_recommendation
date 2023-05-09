def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    t = 0
    for i in range(N):
        t += A[i]
        if t >= T:
            print(i+1, T-(t-A[i]))
            exit()
    T %= t
    t = 0
    for i in range(N):
        t += A[i]
        if t >= T:
            print(i+1, T-(t-A[i]))
            exit()
