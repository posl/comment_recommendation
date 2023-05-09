def main():
    A, B, H, M = map(int, input().split())
    import math
    deg = abs((H*60+M)/2 - M*6)
    if deg > 180:
        deg = 360 - deg
    rad = math.radians(deg)
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(rad))
    print(ans)

if __name__ == '__main__':
    main()