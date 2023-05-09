def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted([(a[i], i) for i in range(n)], reverse=True)
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[i][0]
    print(ans)
main()

if __name__ == '__main__':
    main()