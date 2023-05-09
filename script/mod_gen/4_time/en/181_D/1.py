def main():
    S = input()
    if len(S) == 1:
        if S == '8':
            print('Yes')
        else:
            print('No')
        return
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return
    else:
        count = [0] * 10
        for i in S:
            count[int(i)] += 1
        for i in range(104, 1000, 8):
            c = [0] * 10
            for j in str(i):
                c[int(j)] += 1
            if all([count[k] >= c[k] for k in range(10)]):
                print('Yes')
                return
        print('No')

if __name__ == '__main__':
    main()