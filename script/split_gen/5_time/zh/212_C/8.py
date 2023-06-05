def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10 ** 9
    j = 0
    for i in range(n):
        while j < m - 1 and b[j + 1] <= a[i]:
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
        if j < m - 1:
            ans = min(ans, abs(a[i] - b[j + 1]))
    print(ans)
