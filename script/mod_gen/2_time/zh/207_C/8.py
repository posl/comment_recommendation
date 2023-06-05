def main():
    a,b,c,d = map(int,input().split())
    if b >= a:
        print(-1)
        return
    if d*c-b <= 0:
        print(-1)
        return
    ans = (a//(d*c-b))+1
    print(ans)

if __name__ == '__main__':
    main()