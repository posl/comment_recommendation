def checkLine(points):
    if len(points) < 3:
        return False
    if points[0][0] == points[1][0] == points[2][0]:
        return True
    if points[0][1] == points[1][1] == points[2][1]:
        return True
    if points[0][0] == points[1][0] and points[0][0] == points[2][0]:
        return True
    if points[0][1] == points[1][1] and points[0][1] == points[2][1]:
        return True
    if points[0][0] == points[1][0]:
        if points[0][0] == points[2][0]:
            return True
        return False
    if points[0][1] == points[1][1]:
        if points[0][1] == points[2][1]:
            return True
        return False
    if points[0][1] - points[1][1] == points[0][0] - points[1][0]:
        if points[0][1] - points[2][1] == points[0][0] - points[2][0]:
            return True
        return False
    return False
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
points.sort()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if checkLine([points[i], points[j], points[k]]):
                print("Yes")
                exit()
print("No")

if __name__ == '__main__':
    checkLine()