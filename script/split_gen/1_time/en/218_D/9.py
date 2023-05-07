def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort(key=lambda x:(x[0],x[1]))
    x_dic = {}
    y_dic = {}
    for i in range(N):
        if points[i][0] in x_dic:
            x_dic[points[i][0]].append(points[i][1])
        else:
            x_dic[points[i][0]] = [points[i][1]]
        if points[i][1] in y_dic:
            y_dic[points[i][1]].append(points[i][0])
        else:
            y_dic[points[i][1]] = [points[i][0]]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if points[i][0] == points[j][0]:
                continue
            if points[i][1] == points[j][1]:
                continue
            if points[i][1] in y_dic[points[j][1]]:
                if points[i][0] in x_dic[points[j][0]]:
                    ans += 1
    print(ans)
