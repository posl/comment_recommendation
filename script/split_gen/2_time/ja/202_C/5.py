def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(x) - 1 for x in input().split()]
    d = [0] * n
    for i in range(n):
        d[b[c[i]] - 1] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i] - 1]
    print(ans)
