def main():
    a,b,k = map(int,input().split())
    alist = []
    blist = []
    for i in range(1,101):
        if a % i == 0:
            alist.append(i)
        if b % i == 0:
            blist.append(i)
    alist.reverse()
    blist.reverse()
    #print(alist)
    #print(blist)
    clist = []
    for i in alist:
        for j in blist:
            if i == j:
                clist.append(i)
    #print(clist)
    print(clist[k-1])

if __name__ == '__main__':
    main()