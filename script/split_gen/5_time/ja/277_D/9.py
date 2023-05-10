def solve(n,m,al):
    al.sort()
    print(al)
    #al = al[::-1]
    #print(al)
    ans = 0
    for i in range(n):
        if al[i] % 2 == 0:
            ans += al[i]
        else:
            ans += al[i] - 1
    return ans
n,m = map(int,input().split())
al = list(map(int,input().split()))
print(solve(n,m,al))
