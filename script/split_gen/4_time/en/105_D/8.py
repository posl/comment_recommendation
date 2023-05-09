def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 0
    if sum % m == 0:
        ans += 1
    for i in range(n):
        ans += a[i:].count(m)
    print(ans)
