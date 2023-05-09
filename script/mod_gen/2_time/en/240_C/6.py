def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp1, tmp2 = map(int, input().split())
        a.append(tmp1)
        b.append(tmp2)
    s = 0
    for i in range(n):
        if i % 2 == 0:
            s += a[i]
        else:
            s += b[i]
    if s <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()