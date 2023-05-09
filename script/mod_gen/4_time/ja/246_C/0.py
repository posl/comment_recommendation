def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > x:
            ans += (a[i] - x)
    if k > ans:
        print(0)
    else:
        print(ans - k)

if __name__ == '__main__':
    main()