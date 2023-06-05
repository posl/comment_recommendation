def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    flg = 0
    for i in range(n):
        if s[i] == 'R':
            for j in range(i+1, n):
                if s[j] == 'L':
                    if x[i] == x[j]:
                        if y[i] > y[j]:
                            if flg == 0:
                                flg = 1
                            else:
                                print('Yes')
                                return
                        else:
                            if flg == 0:
                                flg = -1
                            else:
                                print('Yes')
                                return
        else:
            for j in range(i+1, n):
                if s[j] == 'R':
                    if x[i] == x[j]:
                        if y[i] > y[j]:
                            if flg == 0:
                                flg = -1
                            else:
                                print('Yes')
                                return
                        else:
                            if flg == 0:
                                flg = 1
                            else:
                                print('Yes')
                                return
    print('No')
    return

if __name__ == '__main__':
    main()