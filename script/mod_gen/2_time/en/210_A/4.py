def main():
    n,a,x,y = map(int,input().split())
    print(x*min(n,a) + y*max(0,n-a))
main()

if __name__ == '__main__':
    main()