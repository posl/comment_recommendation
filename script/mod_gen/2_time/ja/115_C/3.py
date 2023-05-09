def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = float("inf")
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

if __name__ == '__main__':
    main()