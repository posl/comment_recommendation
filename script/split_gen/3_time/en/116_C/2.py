def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        l = 0
        while l < n and h[l] == 0:
            l += 1
        r = l
        while r < n and h[r] > 0:
            r += 1
        for i in range(l, r):
            h[i] -= 1
        ans += 1
    print(ans)
