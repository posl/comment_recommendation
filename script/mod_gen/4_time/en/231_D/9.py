def solve():
    n,m = map(int,input().split())
    if m == 0:
        print('No')
        return
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab.sort()
    if ab[0][0] == 1:
        print('Yes')
        return
    for i in range(m-1):
        if ab[i][0] == ab[i][1]:
            print('No')
            return
        if ab[i][1] == ab[i+1][0]:
            print('Yes')
            return
    print('No')
solve()
