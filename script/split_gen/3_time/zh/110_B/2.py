def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    z = x+1
    if z<=y:
        if max(x_list)<z and min(y_list)>=z:
            print('No War')
        else:
            print('War')
    else:
        print('War')
