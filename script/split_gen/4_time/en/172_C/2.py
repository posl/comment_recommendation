def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] + a
    b = [0] + b
    for i in range(n):
        a[i+1] += a[i]
    for i in range(m):
        b[i+1] += b[i]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)
