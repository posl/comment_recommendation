def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                if x1 == x2 and x2 == x3:
                    print("Yes")
                    return
                elif y1 == y2 and y2 == y3:
                    print("Yes")
                    return
                elif (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    print("Yes")
                    return
    print("No")
