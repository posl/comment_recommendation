def main():
    L,Q = map(int,input().split())
    c = []
    x = []
    for i in range(Q):
        c_i,x_i = map(int,input().split())
        c.append(c_i)
        x.append(x_i)
    #print(c)
    #print(x)
    L1 = 0
    L2 = L
    for i in range(Q):
        if c[i] == 1:
            if x[i] < L2:
                L2 = x[i]
            if x[i] > L1:
                L1 = x[i]
        if c[i] == 2:
            if x[i] < L2:
                print(L2 - x[i])
            elif x[i] > L1:
                print(x[i] - L1)
            else:
                print(0)
    return 0

if __name__ == '__main__':
    main()