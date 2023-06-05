def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    if k == 1:
        print(n+1)
        return
    if k == 2:
        print((n+1)*(n+2)//2%mod)
        return
    if k == n+1:
        print(1)
        return
    if k == n:
        print(n+1)
        return
    if k == n-1:
        print((n+1)*(n+2)//2%mod)
        return
    if k == n-2:
        print((n+1)*(n+2)*(n+3)//6%mod)
        return
    print(1)

if __name__ == '__main__':
    main()