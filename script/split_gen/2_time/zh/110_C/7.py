def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    for i in range(x+1,y+1):
        if i in x_list and i in y_list:
            print("No War")
            break
    else:
        print("War")
