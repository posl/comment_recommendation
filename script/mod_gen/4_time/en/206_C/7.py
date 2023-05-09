def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n - i - 1) - bisect_right(a, a[i] / 2) + 1
    print(ans)

if __name__ == '__main__':
    main()