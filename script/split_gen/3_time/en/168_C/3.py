def main():
    A, B, H, M = map(int, input().split())
    theta = 2 * math.pi * (H/12 + M/720 - M/60)
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta)))
