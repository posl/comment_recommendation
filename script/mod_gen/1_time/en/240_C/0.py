def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    ans = "No"
    current = 0
    for i in range(n):
        current += a[i]
        if current > x:
            break
        current += b[i]
        if current == x:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()