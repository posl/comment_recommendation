def main():
    n,m = map(int,input().split())
    k = []
    a = []
    for _ in range(m):
        k.append(int(input()))
        a.append(list(map(int,input().split())))
    # print(n,m)
    # print(k)
    # print(a)
    # for i in range(m):
    #     for j in range(k[i]):
    #         print(a[i][j],end=' ')
    #     print()
    # 1. 1~n的数字对应的圆柱体
    # 2. 1~n的数字对应的球
    # 3. 每个圆柱体的球的数量
    # 4. 每个圆柱体的球的颜色
    # 5. 每个圆柱体的球的颜色的数量
    # 6. 每个圆柱体的球的颜色的数量的最小值
    cylinder = [0] * (n+1)
    ball = [0] * (n+1)
    ball_color = [0] * (n+1)
    ball_color_num = [0] * (n+1)
    ball_color_num_min = [0] * (n+1)
    for i in range(m):
        for j in range(k[i]):
            cylinder[a[i][j]] = i+1
            ball[a[i][j]] = j+1
            ball_color[a[i][j]] = a[i][j]
            ball_color_num[a[i][j]] = k[i]
    for i in range(1,n+1):
        ball_color_num_min[i] = ball_color_num[i]
    # print(cylinder)
    # print(ball)
    # print(ball_color)
    # print(ball_color_num)
    # print(ball_color_num_min)
    for i in range(1,n+1):
        if ball_color_num_min[i] > 0:
            for j in range(1,n+1):
                if ball_color_num_min[j] > 0 and ball_color_num_min[i] > 0:
                    if cylinder[i] != cylinder[j] and ball_color[i] == ball_color[j]:
                        ball_color_num_min[i] -= 1
                        ball_color_num_min
