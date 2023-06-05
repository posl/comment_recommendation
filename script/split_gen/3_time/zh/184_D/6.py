def solve(a,b,c):
    ans = 0
    while a>0 and b>0 and c>0:
        ans += 1
        s = a+b+c
        p = [a/s,b/s,c/s]
        a,b,c = [a+1,b+1,c+1]
        a,b,c = [a*p[0],b*p[1],c*p[2]]
        a,b,c = [a-1,b-1,c-1]
    return ans
