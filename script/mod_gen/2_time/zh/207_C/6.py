def main():
    a,b,c,d = map(int,input().split())
    if a > b * d:
        print(-1)
        return
    if d * a <= b:
        print(0)
        return
    if c >= d * b:
        print(-1)
        return
    ans = 0
    while a > b * d:
        a += b
        a -= c
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()