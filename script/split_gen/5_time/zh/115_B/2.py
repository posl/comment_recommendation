def solve():
    n = int(input())
    plist = []
    for i in range(n):
        plist.append(int(input()))
    plist.sort()
    plist.reverse()
    plist[0] = plist[0] / 2
    print(int(sum(plist)))
