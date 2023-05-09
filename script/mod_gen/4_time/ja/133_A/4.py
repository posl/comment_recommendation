def main():
    n,a,b = map(int,input().split())
    ans = 0
    ans = min(a*n,b)
    print(ans)

if __name__ == '__main__':
    main()