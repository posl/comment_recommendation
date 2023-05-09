def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(X)
    y_list.append(Y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0]:
        print("No War")
    else:
        print("War")
