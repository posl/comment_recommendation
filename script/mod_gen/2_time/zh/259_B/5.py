def main():
    n,m,x,t,d = map(int,input().split())
    height = t
    for i in range(1,n):
        if i < x:
            height += d
        elif i == x:
            height += d
        else:
            height += d
    print(height)

if __name__ == '__main__':
    main()