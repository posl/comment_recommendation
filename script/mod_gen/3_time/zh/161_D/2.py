def main():
    K = int(input())
    anslist = []
    for i in range(1, 10):
        anslist.append(i)
    while len(anslist) < K:
        tmp = []
        for i in anslist:
            lastnum = i % 10
            if lastnum == 0:
                tmp.append(i * 10)
                tmp.append(i * 10 + 1)
            elif lastnum == 9:
                tmp.append(i * 10 + 8)
                tmp.append(i * 10 + 9)
            else:
                tmp.append(i * 10 + lastnum - 1)
                tmp.append(i * 10 + lastnum)
                tmp.append(i * 10 + lastnum + 1)
        anslist = tmp
    anslist.sort()
    print(anslist[K - 1])

if __name__ == '__main__':
    main()