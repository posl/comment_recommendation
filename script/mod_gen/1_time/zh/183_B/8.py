def main():
    sx,sy,gx,gy = map(int,input().split())
    x = sx + (gx-sx)*sy/(sy+gy)
    print(x)

if __name__ == '__main__':
    main()