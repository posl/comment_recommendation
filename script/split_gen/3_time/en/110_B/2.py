def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    if X < y_min and x_max < Y:
        for z in range(x_max + 1, y_min + 1):
            if X < z <= Y:
                print('No War')
                break
        else:
            print('War')
    else:
        print('War')
main()
