def main():
    S = input()
    cnt = 0
    for i in range(10000):
        x = str(i).zfill(4)
        flg = True
        for j in range(10):
            if S[j] == 'o' and str(j) not in x:
                flg = False
            if S[j] == 'x' and str(j) in x:
                flg = False
        if flg:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()