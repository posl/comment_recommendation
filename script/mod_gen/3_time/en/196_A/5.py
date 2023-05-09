def main():
    #taking input
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    #finding max of x-y and y-x
    print(max(a-d,b-c))

if __name__ == '__main__':
    main()