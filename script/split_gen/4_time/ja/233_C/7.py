def main():
    n,x = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
        a.append(l[i][1:])
    ans = 0
    for i in range(1,2**n):
        s = 1
        for j in range(n):
            if i&1<<j:
                s*=l[j][0]
        if x%s==0:
            for k in range(n):
                if i&1<<k:
                    for j in range(l[k][0]):
                        if x%s==0:
                            x//=a[k][j]
                        else:
                            break
            if x%s==0:
                ans += 1
    print(ans)
