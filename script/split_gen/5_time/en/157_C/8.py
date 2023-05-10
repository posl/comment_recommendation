def main():
    N, M = map(int, input().split())
    #print(N, M)
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(s, c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            print(-1)
        else:
            if s[0] == 1 and c[0] == 0:
                print(-1)
            else:
                print("{}{}".format(c[0], c[1]))
    elif N == 3:
        if M == 0:
            print(100)
        elif M == 1:
            if s[0] == 1:
                print("{}0".format(c[0]))
            elif s[0] == 2:
                print("{}0".format(c[0]))
            elif s[0] == 3:
                print("0{}".format(c[0]))
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and c[0] == 0 and s[1] == 2 and c[1] == 0:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 3 and c[1] == 0:
                print(-1)
            elif s[0] == 2 and c[0] == 0 and s[1] == 3 and c[1] == 0:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 2 and c[1] == 1:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 3 and c[1] == 1:
                print(-1)
            elif s[0] == 2 and c[0] == 0 and s[1]
