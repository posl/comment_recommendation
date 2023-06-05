def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    ans = 0
    for i in range(n):
        x += a[i]
        ans = max(ans, x)
    print(ans)
main()
