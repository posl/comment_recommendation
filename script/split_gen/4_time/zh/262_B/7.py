def get_num(n, m, uv):
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i+1, j+1) in uv:
                for k in range(j+1, n):
                    if (j+1, k+1) in uv and (i+1, k+1) in uv:
                        num += 1
    return num
