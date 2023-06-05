def main():
    n,x,y = map(int,input().split())
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i<=x and j>=y:
                print(j-i)
            else:
                print(min(j-i,abs(i-x)+1+abs(j-y)))

if __name__ == '__main__':
    main()