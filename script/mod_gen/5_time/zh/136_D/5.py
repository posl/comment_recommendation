def problem136_d():
    s = input()
    n = len(s)
    ans = [0]*n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i-1] += (cnt+1)//2
            cnt = 0
    cnt = 0
    for i in range(n-1,-1,-1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i+1] += (cnt+1)//2
            cnt = 0
    print(' '.join(map(str,ans)))
problem136_d()
