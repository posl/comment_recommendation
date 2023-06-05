def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
    print(ans % (10 ** 9 + 7))
    return

if __name__ == '__main__':
    main()