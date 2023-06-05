def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(a[-1]*a[-2])
    #print(a[0]*a[1])
    if a[-1]*a[-2] <= 0:
        if k <= n*(n-1)//2:
            print(0)
            return
        else:
            print(a[-1]*a[-2])
            return
    if a[0]*a[1] >= 0:
        if k <= n*(n-1)//2:
            print(a[0]*a[1])
            return
        else:
            print(0)
            return
    neg = []
    pos = []
    for i in range(n):
        if a[i] < 0:
            neg.append(a[i])
        else:
            pos.append(a[i])
    #print(neg)
    #print(pos)
    #print(len(neg))
    #print(len(pos))
    if len(neg) == 0 or len(pos) == 0:
        if k <= n*(n-1)//2:
            print(0)
            return
        else:
            print(a[-1]*a[-2])
            return
    if k <= len(neg)*len(pos):
        print(neg[0]*pos[-1])
        return
    else:
        #print(neg[0]*pos[-1])
        #print(neg[-1]*pos[0])
        print(max(neg[0]*pos[-1], neg[-1]*pos[0]))
        return
main()
