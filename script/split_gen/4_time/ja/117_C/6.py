def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(0)
        return
    ans = 0
    for i in range(m-1):
        ans += x[i+1] - x[i]
    ans -= (x[-1] - x[0])
    ans += min(x[0], x[-1])
    print(ans)
