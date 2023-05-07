def main():
    # Get the number of points
    n = int(input())
    # Get the points
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    # Find the line equation of all possible lines
    # y = ax + b
    lines = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            # If the two points are on the same vertical line
            if x1 == x2:
                a = float('inf')
                b = x1
            # If the two points are on the same horizontal line
            elif y1 == y2:
                a = 0
                b = y1
            # If the two points are on the same diagonal line
            elif abs(x1 - x2) == abs(y1 - y2):
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1
            # If the two points are on the same line
            else:
                continue
            # Add the line equation to the list
            lines.append((a, b))
    # Check if there are 3 points on the same line
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            for k in range(j + 1, len(lines)):
                if lines[i] == lines[j] and lines[j] == lines[k]:
                    print('Yes')
                    exit()
    print('No')
