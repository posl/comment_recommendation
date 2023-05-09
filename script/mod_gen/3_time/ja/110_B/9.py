def main():
    n,m,x,y=map(int,input().split())
    x_list=list(map(int,input().split()))
    y_list=list(map(int,input().split()))
    for i in range(x+1,y+1):
        if max(x_list)<i and min(y_list)>=i:
            print("No War")
            return
    print("War")
    return
main()

if __name__ == '__main__':
    main()