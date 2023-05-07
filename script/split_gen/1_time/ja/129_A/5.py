def main():
    P, Q, R = map(int, input().split())
    # P, Q, R = 3, 2, 3
    print(min(P + Q, Q + R, R + P))
