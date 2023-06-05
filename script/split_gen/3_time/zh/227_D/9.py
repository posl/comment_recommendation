def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    ans = 0
    for i in range(n):
        if b[i] >= k:
            ans += 1
    print(ans)
