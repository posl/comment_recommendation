def solve(n,m,ab):
    #n,m = map(int,input().split())
    #ab = [list(map(int,input().split())) for i in range(m)]
    #print(n,m,ab)
    ab.sort(key=lambda x:x[1])
    #print(ab)
    #print(ab[0][1])
    #print(ab[1][1])
    #print(ab[2][1])
    #print(ab[3][1])
    #print(ab[4][1])
    #print(ab[5][1])
    #print(ab[6][1])
    #print(ab[7][1])
    ans = 0
    if ab[0][0] == 1:
        ans += 1
    for i in range(1,m):
        if ab[i][0] >= ab[i-1][1]:
            ans += 1
    return ans
