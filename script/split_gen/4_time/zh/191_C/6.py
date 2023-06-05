def main():
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            count = 0
            for di in range(2):
                for dj in range(2):
                    if S[i+di][j+dj] == '#':
                        count += 1
            if count == 1 or count == 3:
                ans += 1
    print(ans)
