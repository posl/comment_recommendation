def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            cnt = 0
            for k in range(i, i+2):
                for l in range(j, j+2):
                    if S[k][l] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()