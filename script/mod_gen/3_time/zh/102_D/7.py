def process():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    l = 0
    r = s
    ans = float('inf')
    for i in range(n-1):
        l += a[i]
        r -= a[i]
        ans = min(ans, abs(l-r))
    print(ans)

if __name__ == '__main__':
    process()