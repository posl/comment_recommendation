def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 1):
        ans += N - 1 - i - (A[i + 1] - A[i]) * (N - 1 - i)
    print(ans)

if __name__ == '__main__':
    main()