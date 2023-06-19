def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,k,d)
    #print(a)
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = ans//d
    print(ans)

if __name__ == '__main__':
    main()