def main():
    sx, sy, gx, gy = map(int, input().split())
    print((sx * gy + sy * gx) / (sy + gy))

if __name__ == '__main__':
    main()