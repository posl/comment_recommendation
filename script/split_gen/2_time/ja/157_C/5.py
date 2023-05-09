def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(M):
        s_i,c_i = map(int,input().split())
        s.append(s_i)
        c.append(c_i)
    #print(s)
    #print(c)
    if N == 1:
        if M == 0:
            print(0)
        else:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10,99)
        elif M == 1:
            if s[0] == 1:
                print(10*c[0]+0,10*c[0]+9)
            elif s[0] == 2:
                print(10+10*c[0],99+10*c[0])
            else:
                print(-1)
        else:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(10*c[0]+c[1])
                else:
                    print(-1)
            else:
                print(-1)
    else:
        if M == 0:
            print(100,999)
        elif M == 1:
            if s[0] == 1:
                print(100*c[0]+0,100*c[0]+99)
            elif s[0] == 2:
                print(100+10*c[0],999+10*c[0])
            elif s[0] == 3:
                print(100+100*c[0],999+100*c[0])
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                if c[0] == c[1]:
                    print(100*c[0]+c[1])
                else:
                    print(-1)
            elif s[0] == 1 and s[1] == 3:
                if c[0] == c[1]:
                    print(100*c[0]+10*c[1])
                else:
                    print(-1)
            elif s[0] == 2 and s[1] == 3:
                if c[0]
