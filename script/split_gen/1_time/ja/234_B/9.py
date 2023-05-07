def main():
    n = int(input())
    points = []
    for _ in range(n):
        x,y = map(int,input().split())
        points.append([x,y])
    #print(points)
    max_length = 0
    for i in range(n):
        for j in range(i+1,n):
            length = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            max_length = max(max_length,length)
    print(max_length**0.5)
