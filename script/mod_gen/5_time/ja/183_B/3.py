def main():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Gx * Sy + Sx * Gy) / (Sy + Gy))

if __name__ == '__main__':
    main()