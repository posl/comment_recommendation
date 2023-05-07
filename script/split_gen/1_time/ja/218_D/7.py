def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if points[i][0] == points[j][0] and points[j][0] != points[k][0] and points[j][1] != points[k][1]:
                    if points[i][1] < points[j][1] < points[k][1]:
                        ans += 1
                    elif points[i][1] > points[j][1] > points[k][1]:
                        ans += 1
                    elif points[i][1] == points[j][1] and points[j][1] == points[k][1]:
                        ans += 1
    print(ans)
