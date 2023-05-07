def main():
    n = int(input())
    xy = []
    for i in range(n):
        xy.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (xy[i][0] - xy[j][0]) * (xy[j][1] - xy[k][1]) == (xy[j][0] - xy[k][0]) * (xy[i][1] - xy[j][1]):
                    print("Yes")
                    return
    print("No")
