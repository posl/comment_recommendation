def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        ans += (A[i] - A[i - 1]) ** 2
    ans *= N - 1
    for i in range(N):
        ans -= (A[i] * 2) ** 2
    print(ans // 2)

if __name__ == '__main__':
    main()