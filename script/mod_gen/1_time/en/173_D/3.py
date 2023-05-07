def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * (i // 2)
        ans += A[i - 1] * ((i + 1) // 2)
    print(ans)

if __name__ == '__main__':
    main()