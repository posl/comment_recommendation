def main():
    N = int(input())
    x_y = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_y.append((x, y))
    x_y.sort(key=lambda x: x[0])
    x = [x_y[i][0] for i in range(N)]
    y = [x_y[i][1] for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    if x[i] == x[j] and y[k] == y[l]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()