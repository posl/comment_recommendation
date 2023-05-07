def main():
    # input
    N, Q = map(int, input().split())
    Ts = [[0]*3 for _ in range(Q)]
    for i in range(Q):
        Ts[i] = list(map(int, input().split()))
    # compute
    follow = [[False]*(N+1) for _ in range(N+1)]
    for i in range(Q):
        if Ts[i][0] == 1:
            follow[Ts[i][1]][Ts[i][2]] = True
        elif Ts[i][0] == 2:
            follow[Ts[i][1]][Ts[i][2]] = False
        else:
            ans = 'No'
            for j in range(1, N+1):
                if follow[Ts[i][1]][j] and follow[j][Ts[i][2]]:
                    ans = 'Yes'
                    break
            print(ans)
    # output
