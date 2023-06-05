def main():
    a,b,c = map(int,input().split())
    print((a*b*b+b*a*b)/(a*b+b*c+c*a))

if __name__ == '__main__':
    main()