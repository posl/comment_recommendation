def main():
    n,x,y = map(int,input().split())
    ans = [0]*n
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans[min(abs(i-j),abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

if __name__ == '__main__':
    main()