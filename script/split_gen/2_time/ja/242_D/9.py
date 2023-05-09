def main():
    s = input()
    q = int(input())
    l = []
    for i in range(q):
        l.append(input().split())
    #print(l)
    #print(s)
    #print(q)
    for i in range(q):
        t = int(l[i][0])
        k = int(l[i][1])
        #print(t,k)
        if t%3 == 0:
            print(s[k-1])
        elif t%3 == 1:
            if k <= len(s)//3:
                print(s[k-1])
            elif k <= len(s)//3*2:
                print(s[len(s)//3*2+k-1])
            else:
                print(s[k-1])
        else:
            if k <= len(s)//3:
                print(s[len(s)//3*2+k-1])
            elif k <= len(s)//3*2:
                print(s[k-1])
            else:
                print(s[len(s)//3*2+k-1])
