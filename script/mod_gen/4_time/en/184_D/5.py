def main():
    a,b,c = map(int, input().split())
    print((a*b*c)/(a*b+b*c+c*a-a*a-b*b-c*c))

if __name__ == '__main__':
    main()