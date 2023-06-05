def main():
    a,b,c,d = map(int,input().split())
    if a < b:
        print(-1)
        return
    if c >= b*d:
        print(-1)
        return
    ans = 0
    while a > b*d:
        a += b
        a -= c
        ans += 1
    print(ans)
    return
