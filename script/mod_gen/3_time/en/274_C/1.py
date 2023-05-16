def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = ans[A[i] // 2] + 1
        ans[A[i] + 1] = ans[A[i] // 2] + 1
    for i in range(2 * N + 1):
        print(ans[i])

if __name__ == '__main__':
    main()