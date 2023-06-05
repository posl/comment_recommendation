def main():
    num = int(input())
    points = []
    for i in range(num):
        points.append(list(map(int, input().split())))
    max_len = 0
    for i in range(num-1):
        for j in range(i+1, num):
            len = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if len > max_len:
                max_len = len
    print(max_len)
