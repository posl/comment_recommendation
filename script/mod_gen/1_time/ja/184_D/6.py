def main():
    a,b,c = map(int,input().split())
    ans = 0
    ans += a*(c/(a+b+c))
    ans += b*(c/(a+b+c))
    ans += c*(a+b+c-1)/(a+b+c)
    print(ans)

if __name__ == '__main__':
    main()