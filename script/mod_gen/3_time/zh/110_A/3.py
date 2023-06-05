def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*10+b+c,a+b*10+c,a+b+c*10))

if __name__ == '__main__':
    main()