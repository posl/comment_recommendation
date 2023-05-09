def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for j in range(m):
        while i < n and a[i] < b[j]:
            i += 1
        if i < n:
            ans = min(ans, abs(a[i]-b[j]))
        if i > 0:
            ans = min(ans, abs(a[i-1]-b[j]))
    print(ans)
