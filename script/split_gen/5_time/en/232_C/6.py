def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            else:
                if (i in a and j in b) and (i not in c and j not in d):
                    print('No')
                    exit()
                elif (i not in a and j not in b) and (i in c and j in d):
                    print('No')
                    exit()
    print('Yes')
