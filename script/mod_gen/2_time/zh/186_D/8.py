def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

if __name__ == '__main__':
    main()