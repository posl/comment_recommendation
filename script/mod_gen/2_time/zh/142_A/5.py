def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    #print(a)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
        #print(a)
    print(sum(a))

if __name__ == '__main__':
    solve()