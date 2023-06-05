def solve(n,m,ab):
    ab.sort(key=lambda x:x[0])
    count=0
    sum=0
    for i in range(n):
        if count+ab[i][1]<=m:
            count+=ab[i][1]
            sum+=ab[i][0]*ab[i][1]
        else:
            sum+=ab[i][0]*(m-count)
            return sum
    return sum
