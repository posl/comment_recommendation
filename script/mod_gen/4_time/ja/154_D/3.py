def main():
    n,k = map(int,input().split())
    pl = list(map(int,input().split()))
    psum = [0]*(n+1)
    for i in range(n):
        psum[i+1] = psum[i] + pl[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,(psum[i+k]-psum[i])/2)
    print(ans)

if __name__ == '__main__':
    main()