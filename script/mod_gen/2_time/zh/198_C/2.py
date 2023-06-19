def main():
    r, x, y = map(int, input().split())
    if r*r == x*x + y*y:
        print(1)
    elif r*r > x*x + y*y:
        print(2)
    else:
        ans = 0
        while r*r < x*x + y*y:
            ans += 1
            r += r
        print(ans)

if __name__ == '__main__':
    main()