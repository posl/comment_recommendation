def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i * 2 - N + 1)
    print(ans)

if __name__ == '__main__':
    main()