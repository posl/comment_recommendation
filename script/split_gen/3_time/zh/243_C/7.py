def iscollision(n,xy,s):
    for i in range(n):
        if s[i]=='L':
            xy[i][0]=-xy[i][0]
        else:
            xy[i][1]=-xy[i][1]
    xy.sort()
    for i in range(n-1):
        if xy[i][0]==xy[i+1][0]:
            return 'Yes'
    return 'No'
