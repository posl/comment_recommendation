def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += n - 1 - bisect.bisect_left(a, a[i], i+1)
    print(ans)
