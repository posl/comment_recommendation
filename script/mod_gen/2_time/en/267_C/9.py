def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, m)
    #print(a)
    
    #b = [0] * (n-m+1)
    b = []
    for i in range(n-m+1):
        b.append(sum(a[i:i+m]))
    #print(b)
    b.sort()
    #print(b)
    #print(b[-1])
    ans = 0
    for i in range(m):
        ans += (i+1) * b[-1]
    print(ans)
    
solve()

if __name__ == '__main__':
    solve()