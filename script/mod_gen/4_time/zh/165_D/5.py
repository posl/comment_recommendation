def main():
    a,b,n=map(int,input().split())
    print((a*min(b-1,n))//b)

if __name__ == '__main__':
    main()