def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[2*i] = ans[2*i+1] = ans[A[i]] + 1
    print(*ans, sep='
')

if __name__ == '__main__':
    main()