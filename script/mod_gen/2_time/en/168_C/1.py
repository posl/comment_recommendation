def main():
    A, B, H, M = map(int, input().split())
    thetaH = (H * 60 + M) * 360 / (12 * 60)
    thetaM = M * 360 / 60
    theta = abs(thetaH - thetaM)
    ans = (A**2 + B**2 - 2*A*B*math.cos(math.radians(theta))) ** 0.5
    print(ans)

if __name__ == '__main__':
    main()