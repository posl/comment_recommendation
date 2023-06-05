def main():
    n,m = map(int,input().split())
    plist = []
    for i in range(m):
        plist.append(list(input().split()))
    plist.sort(key=lambda x:x[0])
    print(plist)
    ac = 0
    wacount = 0
    for i in range(m):
        if plist[i][1] == 'AC':
            ac += 1
            wacount += int(plist[i][0]) - 1
        else:
            if int(plist[i][0]) - 1 == wacount:
                ac += 1
    print(ac,wacount)
