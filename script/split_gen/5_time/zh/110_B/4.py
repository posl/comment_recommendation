def main():
    n,m,x,y = map(int,input().split())
    x_lst = list(map(int,input().split()))
    y_lst = list(map(int,input().split()))
    for z in range(x+1,y+1):
        if max(x_lst) < z and min(y_lst) >= z:
            print("No War")
            return
    print("War")
