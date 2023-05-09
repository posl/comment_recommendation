def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (xy[j][1] - xy[i][1])/(xy[j][0] - xy[i][0]) <= 1:
                count += 1
    print(count)
