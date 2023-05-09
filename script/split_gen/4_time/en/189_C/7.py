def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in range(1, 100001):
        l = 0
        r = 0
        while l < N:
            while r < N and a[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            l = r
            r = r + 1
    print(ans)
