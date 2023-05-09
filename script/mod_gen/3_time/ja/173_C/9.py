def main():
    H, W, K = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())
    ans = 0
    for row in range(1 << H):
        for col in range(1 << W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if row >> i & 1 == 0 and col >> j & 1 == 0:
                        if C[i][j] == '#':
                            cnt += 1
            if cnt == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()