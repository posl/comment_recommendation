def Main():
    N = int(input())
    for i in range(0, N+1):
        if (N & i) == i:
            print(i)
