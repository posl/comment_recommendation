def main():
    a,b,c,d = map(int, input().split())
    if a <= b:
        print(-1)
        return
    if d*c <= b:
        print(-1)
        return
    ans = 0
    while a > b:
        a += c
        b += d
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()