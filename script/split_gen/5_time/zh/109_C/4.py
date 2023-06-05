def get_max_d(n, x, x_list):
    x_list.append(x)
    x_list.sort()
    d_list = [x_list[i+1] - x_list[i] for i in range(n)]
    #print(d_list)
    return min(d_list)
