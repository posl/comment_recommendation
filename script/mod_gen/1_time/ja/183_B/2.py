def main():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Sx*Gy+Gx*Sy)/(Sy+Gy))

if __name__ == '__main__':
    main()