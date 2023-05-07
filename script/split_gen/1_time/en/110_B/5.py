def main():
    N, M, X, Y = map(int, input().split())
    x_list = [int(x) for x in input().split()]
    y_list = [int(y) for y in input().split()]
    max_x = max(x_list)
    min_y = min(y_list)
    if max_x < min_y:
        if X < max_x < Y:
            if X < min_y <= Y:
                print("No War")
            else:
                print("War")
        else:
            print("War")
    else:
        print("War")
