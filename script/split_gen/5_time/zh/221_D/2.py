def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    d = [0 for i in range(10**9+1)]
    for i in range(n):
        d[a[i]] += 1
        d[a[i]+b[i]] -= 1
    for i in range(1, 10**9+1):
        d[i] += d[i-1]
    for i in range(1, n+1):
        ans = 0
        for j in range(10**9+1):
            if d[j] == i:
                ans += 1
        print(ans, end=' ')
