def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #print(a)
    #print(b)
    c = [0]*n
    for i in range(n):
        c[i] = b[i] - a[i] + 1
    #print(c)
    ans = 1
    for i in range(n):
        ans *= c[i]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    solve()