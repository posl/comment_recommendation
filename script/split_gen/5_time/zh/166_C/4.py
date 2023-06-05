def problems166_c():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, H, AB)
    ans = N
    for i in range(M):
        if H[AB[i][0]-1] >= H[AB[i][1]-1]:
            ans -= 1
        if H[AB[i][0]-1] <= H[AB[i][1]-1]:
            ans -= 1
    print(ans)
problems166_c()
