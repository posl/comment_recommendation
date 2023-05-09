def main():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if LR[j][0] - LR[i][1] >= D:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()