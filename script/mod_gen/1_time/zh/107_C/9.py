def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 8
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) * 2 + max(abs(l), abs(r)))
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)

if __name__ == '__main__':
    main()