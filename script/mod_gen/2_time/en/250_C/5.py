def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(1, N + 1):
        ans[i - 1] = i
    for x in X:
        ans[x - 1], ans[x] = ans[x], ans[x - 1]
    print(*ans)

if __name__ == '__main__':
    main()