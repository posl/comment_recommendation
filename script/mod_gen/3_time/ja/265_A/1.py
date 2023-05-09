def main():
    x,y,n = map(int,input().split())
    ans = 0
    if n%3 == 0:
        ans = (n//3)*y
    elif n%3 == 1:
        ans = ((n//3)*y)+x
    elif n%3 == 2:
        ans = ((n//3)*y)+y-x
    print(ans)

if __name__ == '__main__':
    main()