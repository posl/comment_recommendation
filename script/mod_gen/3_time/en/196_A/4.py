def main():
    #Read input
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    #Find max value of x-y
    max1 = max(b,d)
    min1 = min(a,c)
    print(max1-min1)

if __name__ == '__main__':
    main()