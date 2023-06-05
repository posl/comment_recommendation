def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    a.append(m)
    ans = 0
    for i in range(n):
        d = a[i + 1] - a[i]
        ans += d
        if d > 1:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()