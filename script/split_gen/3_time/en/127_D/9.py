def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a = sorted(a, reverse=True)
    bc = sorted(bc, key=lambda x: x[1], reverse=True)
    ans = 0
    i = 0
    j = 0
    while i < n:
        if j < m and bc[j][0] > 0:
            if a[i] < bc[j][1]:
                ans += bc[j][1]
                bc[j][0] -= 1
            else:
                ans += a[i]
                i += 1
        else:
            ans += a[i]
            i += 1
        if i == n:
            break
        if j == m:
            j = 0
        else:
            j += 1
    print(ans)
