def main():
    n = int(input())
    a = list(map(int, input().split()))
    mid = n // 2
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - a[mid])
    print(ans)
