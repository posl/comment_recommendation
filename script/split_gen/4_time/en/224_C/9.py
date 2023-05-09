def main():
    N = int(input())
    #print(N)
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))
    #print(points)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if isTriangle(points[i],points[j],points[k]):
                    count += 1
    print(count)
