def problem170_c():
    x = int(input().strip())
    n = int(input().strip())
    p = list(map(int,input().strip().split()))
    p.append(x)
    p.sort()
    for i in range(len(p)-1):
        if p[i] == x:
            if abs(p[i-1]-x) <= abs(p[i+1]-x):
                print(p[i-1])
            else:
                print(p[i+1])
            break
