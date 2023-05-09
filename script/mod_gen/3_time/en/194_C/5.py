def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] ** 2 - i * A[i] ** 2
    print(ans)

if __name__ == '__main__':
    main()