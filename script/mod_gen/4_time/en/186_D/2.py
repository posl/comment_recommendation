def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1) - a[i] * i
    print(ans)
main()

if __name__ == '__main__':
    main()