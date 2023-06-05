def main():
    # input
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    # solve
    x.sort()
    if n == 1:
        print(min(abs(x[0]-x[m-1]),abs(x[0]-x[1])))
    else:
        print(min(abs(x[0]-x[m-1]),abs(x[1]-x[m-1]),abs(x[0]-x[m-2]),abs(x[1]-x[m-2])))

if __name__ == '__main__':
    main()