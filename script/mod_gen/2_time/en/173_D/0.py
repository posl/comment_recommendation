def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * (N - i)
    print(ans)

if __name__ == '__main__':
    main()