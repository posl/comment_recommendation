def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        ans = 0
        if x < a:
            while x != a:
                x += 1
                ans += 1
        else:
            while x != a:
                x -= 1
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()