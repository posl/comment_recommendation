def main():
    A, B, H, M = map(int, input().split())
    H = H * 60 + M
    H = H * 360 / (60 * 12)
    M = M * 360 / 60
    print(((A**2 + B**2 - 2*A*B*math.cos(math.radians(H-M)))**0.5))

if __name__ == '__main__':
    main()