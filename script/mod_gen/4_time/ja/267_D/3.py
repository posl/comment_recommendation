def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            tmp = 0
            cnt = 1
            for k in range(i, j + 1):
                tmp += cnt * A[k]
                cnt += 1
            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()