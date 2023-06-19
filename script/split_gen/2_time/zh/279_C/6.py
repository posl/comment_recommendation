def check(S, T):
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] != T[i][j]:
                return False
    return True
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
print("Yes" if check(S, T) else "No")
