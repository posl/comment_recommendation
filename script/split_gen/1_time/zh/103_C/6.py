def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i-1] + a[i]
    ans = 0
    for i in range(n):
        ans += a[i] * i
        ans += b[n-1] - b[i]
    print(ans)
