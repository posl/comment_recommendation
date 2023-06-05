def main():
    n,m = map(int,input().split())
    #print(n,m)
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    #print(s,c)
    if n == 1:
        print(c[0])
    elif n == 2:
        if s[0] == 1:
            print(str(c[0])+str(c[1]))
        else:
            print(str(c[1])+str(c[0]))
    elif n == 3:
        if s[0] == 1:
            print(str(c[0])+str(c[1])+str(c[2]))
        elif s[0] == 2:
            print(str(c[1])+str(c[0])+str(c[2]))
        else:
            print(str(c[1])+str(c[2])+str(c[0]))
    else:
        print(-1)
