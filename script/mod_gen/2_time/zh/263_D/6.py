def printSeq(n,m,l):
    if n == 0:
        print(l)
    else:
        for i in range(1,m+1):
            if len(l) == 0 or i > l[-1]:
                l.append(i)
                printSeq(n-1,m,l)
                l.pop()

if __name__ == '__main__':
    printSeq()