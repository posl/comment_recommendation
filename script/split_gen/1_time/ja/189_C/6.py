def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        l = a[i]
        for j in range(i, n):
            l = min(l, a[j])
            ans = max(ans, l * (j - i + 1))
    print(ans)
