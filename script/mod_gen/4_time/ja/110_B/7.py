def main():
    N,M,X,Y = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    x_max = max(x)
    y_min = min(y)
    if X < y_min and y_min <= Y and x_max < y_min:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()