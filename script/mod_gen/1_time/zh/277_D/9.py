def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*m
    for i in range(n):
        b[a[i]%m] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        ans += 1
        b[i] -= 1
        b[(m-i)%m] -= 1
        ans += max(0,b[i])
    print(ans)
main()
