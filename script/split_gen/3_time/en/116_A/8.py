def main():
    # Read the three sides of the triangle
    a, b, c = map(int, input().split())
    # Calculate the area of the triangle
    area = int(a * b * c / 2)
    # Output the result
    print(area)
