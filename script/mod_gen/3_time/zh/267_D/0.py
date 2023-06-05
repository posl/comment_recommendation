def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((abs(a[i]), a[i]))
    b.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += b[i][1]
    print(ans)

if __name__ == '__main__':
    main()