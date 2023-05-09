def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += 1/n * (1/2)**(len(bin(k-1))-2)
    print(ans)

if __name__ == '__main__':
    main()