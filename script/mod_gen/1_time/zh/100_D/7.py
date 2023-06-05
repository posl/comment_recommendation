def problems100_d():
    n,m = map(int,input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        x_i,y_i,z_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
        z.append(z_i)
    print(x)
    print(y)
    print(z)
    sum_list = []
    for i in range(2**n):
        sum_x = 0
        sum_y = 0
        sum_z = 0
        for j in range(n):
            if ((i>>j)&1):
                sum_x += x[j]
                sum_y += y[j]
                sum_z += z[j]
        sum_list.append([sum_x,sum_y,sum_z])
    print(sum_list)
    max_sum = 0
    for i in range(len(sum_list)):
        for j in range(len(sum_list)):
            for k in range(len(sum_list)):
                if (sum_list[i][0]+sum_list[j][1]+sum_list[k][2])>max_sum:
                    max_sum = sum_list[i][0]+sum_list[j][1]+sum_list[k][2]
    print(max_sum)
problems100_d()
