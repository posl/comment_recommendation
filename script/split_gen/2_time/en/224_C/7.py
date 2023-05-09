def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
        
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if (x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) != 0:
                    count += 1
    print(count)
