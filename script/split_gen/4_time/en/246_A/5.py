def main():
    # Take input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    # Calculate the fourth vertex
    x4 = x3 - (y2 - y1)
    y4 = y3 + (x2 - x1)
    # Print the output
    print(x4, y4)
