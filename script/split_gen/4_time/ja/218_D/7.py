def main():
    n = int(input())
    point = []
    for i in range(n):
        point.append(list(map(int, input().split())))
    point.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if point[i][0] < point[j][0] and point[i][1] < point[j][1]:
                if [point[i][1], point[j][0]] in point and [point[j][1], point[i][0]] in point:
                    count += 1
    print(count)
