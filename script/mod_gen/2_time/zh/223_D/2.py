def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    #print(a)
    #print(b)
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(a[0] + a[1])
        return
    total = 0
    for i in range(n):
        total += a[i] / b[i]
    #print(total)
    half = total / 2
    #print(half)
    for i in range(n):
        if half < a[i] / b[i]:
            print(half * b[i])
            return
        half -= a[i] / b[i]
    print(total - half)

if __name__ == '__main__':
    main()