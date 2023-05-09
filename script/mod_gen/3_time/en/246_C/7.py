def main():
    n, k, x = map(int, input().split())
    ans = 0
    for i in range(n):
        a = int(input())
        if a > x:
            ans += a - x
        if k > 0:
            ans += min(a, x)
            k -= 1
        else:
            ans += a
    print(ans)

if __name__ == '__main__':
    main()