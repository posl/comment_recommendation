def solve():
    #n = int(input())
    #a = list(map(int, input().split()))
    #n, m = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(n)]
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(y[i]-y[j]) <= abs(x[i]-x[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()