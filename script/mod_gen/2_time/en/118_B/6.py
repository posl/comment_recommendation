def main():
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == m:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()