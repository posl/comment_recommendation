def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(m):
        if a[i] < sum * (1/(4*m)):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()