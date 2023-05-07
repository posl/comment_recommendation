def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(N)]
    D.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if i == 0:
            ans += D[i][2] * (D[i][1] - D[i][0] + 1)
        else:
            ans += D[i][2] * (D[i][1] - D[i][0] + 1)
            for j in range(i):
                if D[j][1] >= D[i][0]:
                    ans -= min(D[j][2], D[i][2]) * (D[i][1] - max(D[j][1], D[i][0]) + 1)
    print(ans)

if __name__ == '__main__':
    main()