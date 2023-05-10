def main():
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if TLR[i][1] > TLR[j][1]:
                TLR[i], TLR[j] = TLR[j], TLR[i]
            if TLR[i][2] >= TLR[j][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()