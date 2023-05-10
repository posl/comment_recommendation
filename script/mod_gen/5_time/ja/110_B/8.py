def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0] and x < y_list[0] and y > x_list[-1]:
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()