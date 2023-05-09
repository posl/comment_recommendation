def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    if n == 1:
        if x < p[0]:
            print(x + 1)
            return
        elif x > p[0]:
            print(x - 1)
            return
        else:
            print(x + 1)
            return
    p.sort()
    if x < p[0]:
        print(x)
        return
    if x > p[n - 1]:
        print(x)
        return
    for i in range(n - 1):
        if p[i] < x and x < p[i + 1]:
            if x - p[i] < p[i + 1] - x:
                print(p[i])
                return
            elif x - p[i] > p[i + 1] - x:
                print(p[i + 1])
                return
            else:
                print(p[i])
                return

if __name__ == '__main__':
    main()