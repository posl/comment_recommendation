def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * A[i] - i * A[i]
    print(ans)

if __name__ == '__main__':
    main()