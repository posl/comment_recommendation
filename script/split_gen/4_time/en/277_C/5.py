def problem277_c():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders = sorted(ladders, key=lambda x: x[1])
    print(ladders)
    print(ladders[0][1])
    for i in range(1, N):
        if ladders[i][0] > ladders[i-1][1]:
            print(ladders[i-1][1])
            return
    print(ladders[N-1][1])
