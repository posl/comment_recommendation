def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    current = 0
    for i in range(n):
        current += a[i]
        if current > x:
            print("No")
            return
        current += b[i]
    if current > x:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()