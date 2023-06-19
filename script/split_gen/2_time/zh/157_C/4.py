def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(0,M):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    s_c = list(zip(s,c))
    s_c.sort()
    s,c = zip(*s_c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(0)
        elif M == 1:
            if s[0] == 1:
                print(c[0])
            elif s[0] == 2:
                print(c[0]*10)
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                print(c[0]*10+c[1])
            elif s[0] == 2 and s[1] == 1:
                print(c[1]*10+c[0])
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(0)
        elif M == 1:
            if s[0] == 1:
                print(c[0])
            elif s[0] == 2:
                print(c[0]*10)
            elif s[0] == 3:
                print(c[0]*100)
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and s[1] == 2:
                print(c[0]*10+c[1])
            elif s[0] == 2 and s[1] == 3:
                print(c[0]*10+c[1])
            elif s[0] == 3 and s[1] == 1:
                print(c[1]*100+c[0])
            elif s[0] == 1 and s[1] == 3:
                print(c[0]*100+c[1])
            elif s[0] == 2 and s[1] == 1:
                print(c[1]*10+c
