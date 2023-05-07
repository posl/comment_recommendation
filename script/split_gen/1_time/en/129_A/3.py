def main():
    # Get the input
    P, Q, R = map(int, input().split())
    # Find the minimum of the sum of the flight times
    minSum = min(P + Q, Q + R, R + P)
    # Print the minimum of the sum of the flight times
    print(minSum)
main()
