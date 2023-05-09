def main():
    S = input()
    for i in range(1000):
        if str(i).zfill(3)[-1] != '0' and str(i).zfill(3)[-1] != '8':
            continue
        S1 = S
        for j in str(i).zfill(3):
            if j in S1:
                S1 = S1.replace(j, '', 1)
            else:
                break
        else:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()