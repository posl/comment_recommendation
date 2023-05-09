def main():
    N,M,X,Y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0] and X < y_list[0] and y_list[0] <= Y:
        print("No War")
    else:
        print("War")
main()
