def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        ans += A[i] * i - A[i] * (N - i - 1)
    print(ans)

if __name__ == '__main__':
    main()