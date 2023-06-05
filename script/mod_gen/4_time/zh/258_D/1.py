def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += a[i] + b[i]
    ans += min(a)
    print(ans)

if __name__ == '__main__':
    main()