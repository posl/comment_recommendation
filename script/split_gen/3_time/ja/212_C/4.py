def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        l = 0
        r = M
        while r - l > 1:
            m = (l + r) // 2
            if B[m] <= a:
                l = m
            else:
                r = m
        ans = min(ans, abs(a - B[l]))
        if r < M:
            ans = min(ans, abs(a - B[r]))
    print(ans)
