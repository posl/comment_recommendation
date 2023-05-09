def lunlun(n):
    if n<10:
        return n
    else:
        a = []
        b = []
        for i in range(1,10):
            a.append(i)
        for j in range(n-1):
            b = []
            for k in a[j]:
                if k==0:
                    b.append(k+1)
                elif k==9:
                    b.append(k-1)
                else:
                    b.append(k+1)
                    b.append(k-1)
        a.append(b)
        return a
