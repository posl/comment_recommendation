def main():
    # read input
    n,a,x,y = map(int, input().split())
    # calculate
    if n <= a:
        result = n*x
    else:
        result = a*x + (n-a)*y
    # output
    print(result)

if __name__ == '__main__':
    main()