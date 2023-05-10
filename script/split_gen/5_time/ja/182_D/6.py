def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur)
    print(ans)
