def main():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = 0
    for i in range(N):
        if LR[i][0] <= LR[i][1] - D + 1:
            ans += 1
            LR[i][0] = LR[i][1] - D + 2
            for j in range(i+1, N):
                if LR[j][0] <= LR[i][1] - D + 1:
                    LR[j][0] = LR[i][1] - D + 2
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()