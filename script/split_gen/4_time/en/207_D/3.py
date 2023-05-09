def solve():
    N = int(input())
    S = [list(map(int,input().split())) for i in range(N)]
    T = [list(map(int,input().split())) for i in range(N)]
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(N):
            dx = T[i][0] - S[j][0]
            dy = T[i][1] - S[j][1]
            for k in range(N):
                if [S[k][0] + dx, S[k][1] + dy] not in T:
                    break
            else:
                print("Yes")
                return
    print("No")
    return
