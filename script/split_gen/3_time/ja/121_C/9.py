def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    cnt = 0
    for a,b in ab:
        if cnt + b < m:
            ans += a*b
            cnt += b
        else:
            ans += a*(m-cnt)
            break
    print(ans)
