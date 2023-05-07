def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,len(set(c[i:i+k])))
    print(ans)

if __name__ == '__main__':
    main()