def play_list():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T = T % sum(A)
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i + 1, -T)
            break
play_list()
