def main():
    # Read the input
    A, B = map(int, input().split())
    # Compute the length of the segment (0,0) -> (A,B)
    L = (A**2 + B**2)**0.5
    # Compute the coordinates of the point on the segment (0,0) -> (A,B)
    # whose distance from (0,0) is 1
    x = A/L
    y = B/L
    # Print the coordinates
    print(x, y)
