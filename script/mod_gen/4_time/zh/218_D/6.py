def find_point():
    n = int(raw_input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = raw_input().split()
        x.append(x1)
        y.append(y1)
    x = map(int,x)
    y = map(int,y)
    x.sort()
    y.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                for k in range(j+1,n):
                    if y[k] == y[j]:
                        for l in range(k+1,n):
                            if y[l] == y[k] and x[l] == x[i]:
                                count += 1
    print count
find_point()
