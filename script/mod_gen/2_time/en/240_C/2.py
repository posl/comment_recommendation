def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    s = 0
    for i in range(n):
        s += a[i]
        if s <= x and x <= s + b[i]:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()