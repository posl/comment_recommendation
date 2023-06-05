def main():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append(list(map(int,input().split())))
    t0 = 0
    x0 = 0
    for i in range(n):
        t = txa[i][0]
        x = txa[i][1]
        a = txa[i][2]
        if (t - t0) < abs(x - x0):
            print('No')
            return
        if (t - t0) % 2 != abs(x - x0) % 2:
            print('No')
            return
        t0 = t
        x0 = x
    print('Yes')

if __name__ == '__main__':
    main()