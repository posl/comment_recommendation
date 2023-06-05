def main():
    W,H,x,y = map(int,input().split())
    max_area = W*H/2
    if x == W/2 and y == H/2:
        print(max_area,1)
    else:
        print(max_area,0)

if __name__ == '__main__':
    main()