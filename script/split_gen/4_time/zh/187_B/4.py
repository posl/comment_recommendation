def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                cnt += 1
    print(cnt)
