def main():
    x = input()
    if len(x) == 1:
        if int(x) % 8 == 0:
            print('Yes')
            return
        else:
            print('No')
            return
    elif len(x) == 2:
        if int(x) % 8 == 0:
            print('Yes')
            return
        elif int(x[1] + x[0]) % 8 == 0:
            print('Yes')
            return
        else:
            print('No')
            return
    else:
        d = dict()
        for i in range(1, 10):
            d[str(i)] = 0
        for i in x:
            d[i] += 1
        for i in range(112, 1000, 8):
            check = True
            d_temp = dict()
            for j in range(1, 10):
                d_temp[str(j)] = 0
            for j in str(i):
                d_temp[j] += 1
            for j in range(1, 10):
                if d[str(j)] < d_temp[str(j)]:
                    check = False
            if check:
                print('Yes')
                return
        print('No')

if __name__ == '__main__':
    main()