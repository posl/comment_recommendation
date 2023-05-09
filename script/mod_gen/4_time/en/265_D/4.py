def solve():
    n,p,q,r = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] >= p:
            break
        for j in range(i+1,n):
            if a[j] >= q:
                break
            for k in range(j+1,n):
                if a[k] >= r:
                    break
                for l in range(k+1,n):
                    if a[i] + a[j] + a[k] + a[l] == p + q + r:
                        ans += 1
    print("Yes" if ans else "No")

if __name__ == '__main__':
    solve()