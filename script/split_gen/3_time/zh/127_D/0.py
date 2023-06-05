def p127_d():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    bc = [list(map(int,input().split())) for _ in range(m)]
    bc.sort(key=lambda x:x[1],reverse=True)
    i = 0
    for b,c in bc:
        for _ in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
                if i >= n:
                    break
            else:
                break
        if i >= n:
            break
    print(sum(a))
