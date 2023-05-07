def main():
    x,y,n = map(int,input().split())
    #print(x,y,n)
    ans = 0
    while n > 0:
        if n%3 == 0:
            ans += y
            n -= 3
        else:
            ans += x
            n -= 1
    print(ans)

if __name__ == '__main__':
    main()