def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i]
    ans -= n - 1
    print(ans)
