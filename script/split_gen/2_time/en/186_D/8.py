def main():
    n = int(input())
    a = list(map(int, input().split()))
    # sort a
    a.sort()
    # compute the sum of |a_i-a_j| for all pairs (i, j) where 1 <= i < j <= n
    ans = 0
    for i in range(n - 1):
        ans += (n - i - 1) * a[i]
        ans -= i * a[i]
    print(ans)
