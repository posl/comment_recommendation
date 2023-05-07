def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d * c <= b:
        print(0)
        return
    if a <= c * d - b:
        print(-1)
        return
    ans = (a - b + c - d - 1) // (c - d)
    print(ans)

if __name__ == '__main__':
    main()