def main():
    S = input()
    if len(S) == 1:
        if S == '8':
            print('Yes')
        else:
            print('No')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        num = [0]*10
        for i in S:
            num[int(i)] += 1
        for i in range(112, 1000, 8):
            tmp = [0]*10
            for j in str(i):
                tmp[int(j)] += 1
            flag = True
            for j in range(10):
                if tmp[j] > num[j]:
                    flag = False
                    break
            if flag:
                print('Yes')
                exit()
        print('No')

if __name__ == '__main__':
    main()