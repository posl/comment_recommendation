def main():
    n,x,y = map(int,input().split())
    x -= 1
    y -= 1
    ans = [0] * n
    for i in range(n):
        for j in range(i+1,n):
            d = min(j-i,abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))
            ans[d] += 1
    for i in range(1,n):
        print(ans[i])

if __name__ == '__main__':
    main()