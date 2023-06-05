def main():
    n,m,x,y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.sort()
    y_list.sort()
    if x < y and x_list[-1] < y and y_list[0] >= y:
        print("No War")
    else:
        print("War")
