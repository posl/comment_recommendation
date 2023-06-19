def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for a,b in ab:
        ans += a*b
        m -= b
        if m <= 0:
            ans -= m*a
            break
    print(ans)
