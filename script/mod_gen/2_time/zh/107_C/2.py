def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            time = min(abs(l), abs(r)) + r - l
        else:
            time = max(abs(l), abs(r))
        ans = min(ans, time)
    print(ans)

if __name__ == '__main__':
    main()