def main():
    n = int(input())
    s = input()
    q = int(input())
    t = []
    a = []
    b = []
    for i in range(q):
        tt, aa, bb = map(int, input().split())
        t.append(tt)
        a.append(aa)
        b.append(bb)
    #print(t)
    #print(a)
    #print(b)
    #print(s)
    for i in range(q):
        if t[i] == 1:
            if a[i] <= n:
                aa = a[i] - 1
            else:
                aa = a[i] - 1 - n
            if b[i] <= n:
                bb = b[i] - 1
            else:
                bb = b[i] - 1 - n
            ss = s[aa]
            s = s[:aa] + s[bb] + s[aa+1:]
            s = s[:bb] + ss + s[bb+1:]
        else:
            ss = s[:n]
            s = s[n:] + ss
        #print(s)
    print(s)
