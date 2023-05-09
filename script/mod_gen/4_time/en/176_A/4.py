def main():
    n,x,t = [int(i) for i in input().split()]
    print((n+x-1)//x*t)

if __name__ == '__main__':
    main()