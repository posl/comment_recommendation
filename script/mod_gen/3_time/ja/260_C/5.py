def main():
    n,x,y = map(int,input().split())
    ans = 0
    if x > y:
        ans = x*(n-1)
    else:
        ans = x*(n-1)+y*(n-2)
    print(ans)

if __name__ == '__main__':
    main()