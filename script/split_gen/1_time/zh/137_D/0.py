def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort()
    #print(ab)
    ans = 0
    i = 0
    while m > 0:
        if i >= n:
            break
        a, b = ab[i]
        if m >= a:
            ans += b
            m -= a
        else:
            break
        i += 1
    print(ans)
