def main():
    a,b,x = map(int,input().split())
    if a * 10**9 + b * 10 > x:
        print(0)
    else:
        print(10**9)

if __name__ == '__main__':
    main()