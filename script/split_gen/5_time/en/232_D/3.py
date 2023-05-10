def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                if C[i][j] == '.':
                    ans += 1
            else:
                if C[i][W-j-1] == '.':
                    ans += 1
    print(ans)
