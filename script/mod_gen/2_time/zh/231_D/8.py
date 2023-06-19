def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] < b[0] and b[0] < a[1] and a[1] < b[1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()