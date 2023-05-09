def main():
    # Get input
    P,Q,R = input().split()
    P = int(P)
    Q = int(Q)
    R = int(R)
    # Find the minimum of the sum of the flight times
    min = P + Q
    if min > P + R:
        min = P + R
    if min > Q + R:
        min = Q + R
    # Print the minimum of the sum of the flight times
    print(min)
