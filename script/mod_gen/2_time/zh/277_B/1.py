def main():
    n,x=map(int,input().split())
    p=list(map(int,input().split()))
    print(p.index(x)+1)

if __name__ == '__main__':
    main()