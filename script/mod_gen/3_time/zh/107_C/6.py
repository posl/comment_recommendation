def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        left = x[i]
        right = x[i+k-1]
        ans = min(ans,min(abs(left),abs(right))+right-left)
    print(ans)

if __name__ == '__main__':
    main()