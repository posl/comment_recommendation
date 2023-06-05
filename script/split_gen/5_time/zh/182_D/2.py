def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i]
    print(ans)
