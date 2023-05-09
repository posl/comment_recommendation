def main():
    n,x,y = map(int, input().split())
    ans = [0]*(n-1)
    for i in range(1,n):
        for j in range(i+1,n+1):
            tmp = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            ans[tmp-1] += 1
    for i in range(n-1):
        print(ans[i])

if __name__ == '__main__':
    main()