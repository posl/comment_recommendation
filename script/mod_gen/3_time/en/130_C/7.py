def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x == W/2 and y == H/2:
        cut = 1
    else:
        cut = 0
    print(area,cut)

if __name__ == '__main__':
    main()