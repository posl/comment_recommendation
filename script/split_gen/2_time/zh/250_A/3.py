def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n+1)
    c = [0] * (n+1)
    for i in range(1, n+1):
        b[a[i]] += 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            c[i * a[j]] += b[i]
    ans = 0
    for i in range(1, n+1):
        ans += c[i]
    print(ans)
