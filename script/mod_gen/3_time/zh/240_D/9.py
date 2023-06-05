def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(n):
        b.append(a[i])
        if i == 0:
            c.append(1)
        else:
            c.append(c[i - 1] + 1)
        while len(b) >= 2 and b[-1] == b[-2]:
            b.pop()
            b.pop()
            c[-1] = c[-1] + c[-2]
            c.pop()
            c.pop()
            if len(b) == 0:
                break
    for i in range(n):
        print(c[i])

if __name__ == '__main__':
    main()