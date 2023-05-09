def main():
    a,b,c,d = map(int,input().split())
    if b >= c*d:
        print(-1)
        return
    ans = 0
    while True:
        if a <= 0:
            break
        a += b
        a -= c
        ans += 1
    print(ans)
