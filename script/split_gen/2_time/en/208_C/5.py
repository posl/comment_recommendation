def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    if k >= n:
        for i in range(n):
            ans[i] += k // n
        k = k % n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[i] + (k + a[i] - 1) // a[i])
