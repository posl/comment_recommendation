def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(N, M, s, c)
    #print(len(s), len(c))
    #print(s.index(1))
    #print(c[s.index(1)])
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
            print(10+c[0])
        elif M == 2:
            print(c[0]*10+c[1])
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100)
        elif M == 1:
            print(100+c[0]*10)
        elif M == 2:
            print(100+c[0]*10+c[1])
        elif M == 3:
            print(c[0]*100+c[1]*10+c[2])
        else:
            print(-1)
    else:
        print(-1)
