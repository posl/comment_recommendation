def main():
    x,n = map(int,input().split())
    p = set(map(int,input().split()))
    if n == 0:
        print(x)
        return
    ans = 0
    for i in range(100):
        if not x - i in p:
            ans = x - i
            break
        if not x + i in p:
            ans = x + i
            break
    print(ans)

if __name__ == '__main__':
    main()