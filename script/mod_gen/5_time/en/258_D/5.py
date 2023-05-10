def main():
    # input
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # solve
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans = max(ans, AB[i][0] + AB[i][1] * (X - 1))
    # output
    print(ans)

if __name__ == '__main__':
    main()