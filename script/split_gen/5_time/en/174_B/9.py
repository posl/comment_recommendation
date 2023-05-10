def main():
    # Get the number of points and the radius
    n, d = map(int, input().split())
    # Initialize the counter
    c = 0
    # Loop through the points
    for i in range(n):
        # Get the point
        x, y = map(int, input().split())
        # Check if the distance is less than or equal to the radius
        if x**2 + y**2 <= d**2:
            # Increment the counter
            c += 1
    # Print the number of points
    print(c)
