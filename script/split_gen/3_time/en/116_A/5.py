def main():
    # Read the three sides of the triangle
    AB, BC, CA = map(int, input().split())
    # Calculate the area of the triangle
    area = (AB*BC)//2
    # Print the area of the triangle
    print(area)
