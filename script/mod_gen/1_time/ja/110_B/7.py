def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    X = max(x)
    Y = min(y)
    if(X < Y):
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()