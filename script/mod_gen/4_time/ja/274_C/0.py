def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = i + 1
    for i in range(N, 0, -1):
        ans[i] = ans[2 * i] + ans[2 * i + 1]
    for i in range(1, 2 * N + 1):
        print(ans[i])

if __name__ == '__main__':
    main()