def solve():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    S.sort()
    T.sort()
    S = [[S[i][0]-S[0][0], S[i][1]-S[0][1]] for i in range(N)]
    T = [[T[i][0]-T[0][0], T[i][1]-T[0][1]] for i in range(N)]
    if S == T:
        print("Yes")
        return
    for i in range(N):
        for j in range(N):
            if S[i][0] == T[j][0] and S[i][1] == T[j][1]:
                S = [S[k] for k in range(N) if k != i]
                T = [T[k] for k in range(N) if k != j]
                if S == T:
                    print("Yes")
                    return
                break
    print("No")
    return
