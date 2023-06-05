def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float('inf')
    cur = 0
    for i in range(n - 1):
        cur += a[i]
        ans = min(ans, abs(s - 2 * cur))
    print(ans)
