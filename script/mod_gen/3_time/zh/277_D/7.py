def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0] * (m+1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        if b[i+1] == 0:
            ans += i+1
            b[i+1] += 1
        b[i+1] -= 1
        b[i] -= 1
    print(ans)
main()
