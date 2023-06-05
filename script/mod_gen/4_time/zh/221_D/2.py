def main():
    N = int(input())
    login = []
    for i in range(N):
        A, B = map(int, input().split())
        login.append([A, B])
    login.sort()
    login.append([10 ** 9 + 1, 0])
    ans = [0] * (N + 1)
    cnt = 0
    day = login[0][0]
    for i in range(N):
        if login[i][0] != day:
            ans[cnt] += login[i][0] - day
            day = login[i][0]
        cnt += login[i][1]
        if login[i + 1][0] != day:
            ans[cnt] += 1
    print(*ans[1:])

if __name__ == '__main__':
    main()