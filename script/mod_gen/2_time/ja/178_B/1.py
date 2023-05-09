def main():
    a,b,c,d = map(int,input().split())
    ans = max(a*c,a*d,b*c,b*d)
    print(ans)

if __name__ == '__main__':
    main()