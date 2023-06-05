def main():
    n,x,y = map(int, input().split())
    n -= 1
    x -= 1
    y -= 1
    ans = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            ans[min(j-i,abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(ans[i])

if __name__ == '__main__':
    main()