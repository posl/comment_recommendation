def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i * 2 - n + 1)
    print(ans)

if __name__ == '__main__':
    main()