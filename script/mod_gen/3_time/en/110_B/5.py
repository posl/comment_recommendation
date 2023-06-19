def main():
    #N, M, X, Y = map(int, input().split())
    #x = list(map(int, input().split()))
    #y = list(map(int, input().split()))
    N, M, X, Y = 5, 3, 6, 8
    x = [-10, 3, 1, 5, -100]
    y = [100, 6, 14]
    x.sort()
    y.sort()
    if x[-1] < y[0] and x[-1] < Y and y[0] > X:
        print("No War")
    else:
        print("War")
main()
