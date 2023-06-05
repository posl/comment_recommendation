def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    if n < m:
        print("No")
        return
    i = 0
    for j in range(m):
        while i < n:
            if b[j] <= a[i]:
                i += 1
                break
            else:
                i += 1
        if i == n:
            print("No")
            return
    print("Yes")
solve()
