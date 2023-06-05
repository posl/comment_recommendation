def solve(n,k,a):
    a = [i-1 for i in a]
    s = [1]
    c = [0]*n
    c[0] = 1
    while c[s[-1]] == 0:
        s.append(a[s[-1]])
        c[s[-1]] = c[s[-2]]+1
    l = c[s[-1]]-1
    r = len(s)-1
    if k < l:
        print(s[k]+1)
    else:
        print(s[(k-l)%(r-l)+l]+1)
