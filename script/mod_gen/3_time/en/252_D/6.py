def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += bisect.bisect_left(a, a[i] + 3) - i - 1
    print(ans)

if __name__ == '__main__':
    main()