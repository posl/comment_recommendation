def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - i - 1 for i in range(n)]
    a.sort()
    b = a[n // 2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)
