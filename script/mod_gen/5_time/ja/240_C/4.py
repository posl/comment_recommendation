def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(n):
        if a[i] <= x:
            pos += 1
        else:
            pos -= 1
    if pos >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()