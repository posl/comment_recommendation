def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * pow(L, i) + A[i] * pow(R, N - i - 1)
    print(ans)

if __name__ == '__main__':
    main()