def main():
    n,x,t = map(int,input().split())
    print((n//x + (n%x>0))*t)

if __name__ == '__main__':
    main()