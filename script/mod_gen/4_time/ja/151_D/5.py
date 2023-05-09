def main():
    H,W = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += 1
    if ans == H+W-1:
        ans = ans - 1
    print(ans)

if __name__ == '__main__':
    main()