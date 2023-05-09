def solve(n,m,k,s,p):
    ans = 0
    for i in range(2**n):
        ok = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    return ans
n,m = map(int, input().split())
k = []
s = []
for i in range(m):
    k.append(0)
    s.append([])
for i in range(m):
    a = list(map(int, input().split()))
    k[i] = a[0]
    for j in range(k[i]):
        s[i].append(a[j+1])
p = list(map(int, input().split()))
print(solve(n,m,k,s,p))

if __name__ == '__main__':
    solve()