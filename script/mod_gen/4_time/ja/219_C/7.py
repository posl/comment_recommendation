def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    #print(x)
    #print(n)
    #print(s)
    xlist = list(x)
    xdict = {}
    for i in range(len(xlist)):
        xdict[xlist[i]] = chr(i+97)
    #print(xdict)
    sdict = {}
    for i in range(n):
        slist = list(s[i])
        sdict[s[i]] = ''
        for j in range(len(slist)):
            sdict[s[i]] += xdict[slist[j]]
    #print(sdict)
    sdict = sorted(sdict.items(), key=lambda x:x[1])
    #print(sdict)
    for i in range(n):
        print(sdict[i][0])

if __name__ == '__main__':
    main()