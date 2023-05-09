def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += N - i - 1 - A[i:].count(A[i])
    print(ans)
main()

if __name__ == '__main__':
    main()