def main():
    n = int(raw_input())
    plist = []
    for i in xrange(n):
        plist.append(int(raw_input()))
    plist.sort(reverse=True)
    plist[0] = plist[0] / 2
    print sum(plist)
