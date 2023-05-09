def solve():
    # a,b = list(map(int,input().split()))
    # c = list(map(int,input().split()))
    # s = input()
    # h = [list(map(int,input().split())) for i in range(n)]
    # c = list(map(int,input().split()))
    # s = input()
    # h = [list(map(int,input().split())) for i in range(n)]
    d,g = list(map(int,input().split()))
    p = []
    c = []
    for i in range(d):
        a,b = list(map(int,input().split()))
        p.append(a)
        c.append(b)
    ans = 10000000000000
    for i in range(2**d):
        sum = 0
        cnt = 0
        for j in range(d):
            if (i>>j)&1:
                sum += p[j]*(j+1)*100+c[j]
                cnt += p[j]
        if sum >= g:
            ans = min(ans,cnt)
        else:
            for j in range(d-1,-1,-1):
                if (i>>j)&1:
                    continue
                for k in range(p[j]):
                    if sum >= g:
                        break
                    sum += (j+1)*100
                    cnt += 1
            ans = min(ans,cnt)
    print(ans)

if __name__ == '__main__':
    solve()