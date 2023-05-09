def main():
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(n)]
    point.sort()
    slope = []
    for i in range(n-1):
        for j in range(i+1, n):
            #print(point[i][0], point[i][1], point[j][0], point[j][1])
            if point[i][0] != point[j][0]:
                slope.append((point[j][1]-point[i][1])/(point[j][0]-point[i][0]))
    slope.sort()
    ans = 0
    for i in range(len(slope)-1):
        if slope[i] >= -1 and slope[i] <= 1:
            ans += 1
    print(ans)
