def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * n
    for i in b:
        c[i - 1] = 1
    d = []
    for i in range(n):
        if c[i] == 0:
            d.append(a[i])
    if len(d) == 0:
        print('No')
    else:
        d.sort()
        if d[-1] > a[-1]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()