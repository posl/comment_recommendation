def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j), abs(Y - i) + 1 + abs(X - j))
            ans[d] += 1
    print(*ans[1:], sep="\n")

if __name__ == '__main__':
    main()