def problem177_a():
    d,t,s = map(int,input().split())
    if d <= t*s:
        print('Yes')
    else:
        print('No')
