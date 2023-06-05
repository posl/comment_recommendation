def problems152_c():
    N = int(input())
    P = list(map(int, input().split()))
    result = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            result += 1
            min = P[i]
    print(result)
problems152_c()
