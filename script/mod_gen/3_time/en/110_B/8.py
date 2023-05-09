def main():
    # Read data
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # Check conditions
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()