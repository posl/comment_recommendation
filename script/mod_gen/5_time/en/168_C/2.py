def main():
    import math
    A, B, H, M = map(int, input().split())
    angle = abs(30*H - 5.5*M)
    if angle > 180:
        angle = 360 - angle
    ans = (A**2 + B**2 - 2*A*B*math.cos(math.radians(angle)))**0.5
    print(ans)

if __name__ == '__main__':
    main()