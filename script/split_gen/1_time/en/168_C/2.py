def main():
    A, B, H, M = map(int, input().split())
    theta = abs(30*H - 5.5*M)
    print((A**2 + B**2 - 2*A*B*math.cos(math.radians(theta)))**0.5)
