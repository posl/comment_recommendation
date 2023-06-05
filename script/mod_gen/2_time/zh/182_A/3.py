def main():
    s = input()
    if len(s) == 1:
        if s == '8':
            print('Yes')
        else:
            print('No')
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        a = [0 for i in range(10)]
        for i in s:
            a[int(i)] += 1
        for i in range(112, 1000, 8):
            b = [0 for j in range(10)]
            for j in str(i):
                b[int(j)] += 1
            flag = True
            for j in range(10):
                if a[j] < b[j]:
                    flag = False
            if flag:
                print('Yes')
                return
        print('No')

if __name__ == '__main__':
    main()