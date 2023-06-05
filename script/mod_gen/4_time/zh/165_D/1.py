def main():
    a,b,n = map(int,input().split())
    x = min(n,b-1)
    print(a*x//b-a*(x//b))

if __name__ == '__main__':
    main()