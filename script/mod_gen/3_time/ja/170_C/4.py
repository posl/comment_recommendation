def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    if x <= p[0]:
        print(p[0])
        return
    if p[-1] <= x:
        print(p[-1])
        return
    for i in range(n):
        if p[i] <= x < p[i+1]:
            if x-p[i] <= p[i+1]-x:
                print(p[i])
                return
            else:
                print(p[i+1])
                return

if __name__ == '__main__':
    main()