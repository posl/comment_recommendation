def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        x = 1
        while i < k:
            i *= 2
            x *= 0.5
        ans += x
    ans /= n
    print(ans)

if __name__ == '__main__':
    main()