def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, 360 - a[i])
    print(ans)
