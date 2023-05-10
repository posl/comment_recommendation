def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + b[i-1]
    ans = 0
    for i in range(1, m+1):
        ans = max(ans, b[i-1] + i * b[n-1] - b[n-i-1])
    print(ans)
