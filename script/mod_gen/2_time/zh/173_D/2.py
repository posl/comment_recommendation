def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
    ans -= max(a)
    ans -= max(a)
    print(ans)

if __name__ == '__main__':
    main()