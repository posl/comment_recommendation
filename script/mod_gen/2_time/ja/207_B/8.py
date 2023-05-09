def main():
    a,b,c,d = map(int,input().split())
    ans = 0
    while True:
        if a > c*d:
            ans = -1
            break
        elif a <= c*d:
            if a + b <= c*d:
                a += b
                ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()