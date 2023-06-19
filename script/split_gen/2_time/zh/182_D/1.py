def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(n):
        x += a[i]
        ans = max(ans, x)
    print(ans)
