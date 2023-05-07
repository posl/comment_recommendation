def main():
    # Get the input
    AB, BC, CA = map(int, input().split())
    # Calculate the area
    area = (AB * BC) // 2
    # Output the result
    print(area)
