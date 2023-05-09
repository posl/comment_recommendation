def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    #print(points)
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            #print(x1, y1, x2, y2)
            len = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            if max_len < len:
                max_len = len
    print(max_len)

if __name__ == '__main__':
    main()