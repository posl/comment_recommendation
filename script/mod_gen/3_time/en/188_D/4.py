def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort()
    ans = 0
    for i in range(N):
        ans += ABC[i][2] * (ABC[i][1] - ABC[i][0] + 1)
    ans += C * (ABC[-1][1] - ABC[0][0] + 1)
    for i in range(N - 1):
        ans -= ABC[i][2] * (ABC[i + 1][0] - ABC[i][1] - 1)
    print(ans)

if __name__ == '__main__':
    main()