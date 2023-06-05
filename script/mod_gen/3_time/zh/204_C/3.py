def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        ans += a[i] - a[0] + 1
        ans += b[i] - b[0] + 1
    ans -= m
    print(ans)

if __name__ == '__main__':
    main()