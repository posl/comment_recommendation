def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        b[i] = max(0, b[i] - a[i])
        ans += min(a[i+1], b[i])
        a[i+1] = max(0, a[i+1] - b[i])
    print(ans)
