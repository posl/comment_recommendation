def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    if total <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()