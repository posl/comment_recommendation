def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    if n == 1:
        print(1)
        print(0)
        print('U')
        return
    if n == 2:
        if x[0] == x[1]:
            print(1)
            print(abs(y[0] - y[1]))
            if y[0] > y[1]:
                print('D')
            else:
                print('U')
        elif y[0] == y[1]:
            print(1)
            print(abs(x[0] - x[1]))
            if x[0] > x[1]:
                print('L')
            else:
                print('R')
        else:
            print(-1)
        return
    if n == 3:
        if x[0] == x[1] and x[0] == x[2]:
            print(1)
            print(abs(y[0] - y[1]) + abs(y[1] - y[2]))
            if y[0] > y[1]:
                print('D')
            else:
                print('U')
            if y[1] > y[2]:
                print('D')
            else:
                print('U')
        elif y[0] == y[1] and y[0] == y[2]:
            print(1)
            print(abs(x[0] - x[1]) + abs(x[1] - x[2]))
            if x[0] > x[1]:
                print('L')
            else:
                print('R')
            if x[1] > x[2]:
                print('L')
            else:
                print('R')
        else:
            print(-1)
        return
    if n == 4:
        if x[0] == x[1] and x[0] == x[2] and x[0] == x[3]:
            print(1)
            print(abs(y[0] - y[1]) + abs(y[1] - y[2]) + abs(y[2] - y[3]))
            if y[0] > y[1]:
                print('D')
            else:

if __name__ == '__main__':
    main()