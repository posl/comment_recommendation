def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    if n == 1:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print(2)
                print(1, 1)
                print('UD')
                print('DU')
                return
    if n == 2:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if x[i] == x[j] == x[k] or y[i] == y[j] == y[k]:
                    print(3)
                    print(1, 1, 1)
                    print('UDL')
                    print('DUL')
                    print('LUR')
                    return
    if n == 3:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if x[i] == x[j] == x[k] == x[l] or y[i] == y[j] == y[k] == y[l]:
                        print(4)
                        print(1, 1, 1, 1)
                        print('UDLR')
                        print('DULR')
                        print('LURD')
                        print('RDLU')
                        return
    print(5)
    print(1, 1, 1, 1, 1)
    print('UDLRL')
    print('DULRL')
    print('LURDL')
    print('RDLUR')
    print('LRDLU')
main()
