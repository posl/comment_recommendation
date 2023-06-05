def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print(int((a*x)/b)-a*int(x/b))

if __name__ == '__main__':
    main()