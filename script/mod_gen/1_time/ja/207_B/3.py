def main():
    a, b, c, d = map(int, input().split())
    if a <= b * d:
        print(-1)
        return
    ans = 0
    while a > c * d:
        a += b
        c += d
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()