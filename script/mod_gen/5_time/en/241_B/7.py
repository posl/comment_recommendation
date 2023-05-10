def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        print("No")
    elif m == n:
        if a == b:
            print("Yes")
        else:
            print("No")
    elif m < n:
        a.sort()
        b.sort()
        c = []
        for i in range(n):
            if a[i] in b:
                c.append(a[i])
        if c == b:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()