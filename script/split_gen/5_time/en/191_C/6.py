def main():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    ans -= (H+W-1)
    print(ans)
