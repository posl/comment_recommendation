def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            max_len = max(max_len, ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5)
    print(max_len)
