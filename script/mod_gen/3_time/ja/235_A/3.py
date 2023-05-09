def main():
    a,b,c = map(int,input().split())
    print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)

if __name__ == '__main__':
    main()