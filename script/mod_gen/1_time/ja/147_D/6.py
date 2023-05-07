def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(60):
        c = 0
        for j in range(N):
            if A[j] & 1 << i:
                c += 1
        ans += c * (N - c) * pow(2, i, 10 ** 9 + 7)
        ans %= 10 ** 9 + 7
    print(ans)

if __name__ == '__main__':
    main()