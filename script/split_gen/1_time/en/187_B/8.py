def main():
    N = int(input())
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = points[i]
            x2,y2 = points[j]
            if x1 == x2:
                continue
            slope = (y1 - y2)/(x1 - x2)
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)
