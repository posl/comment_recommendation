def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x*2 == W and y*2 == H:
        print(area,1)
    else:
        print(area,0)

if __name__ == '__main__':
    main()