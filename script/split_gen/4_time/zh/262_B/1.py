def get_num_of_triangle(n, m, e):
    answer = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if e[i][j] == 1:
                for k in range(j+1, n+1):
                    if e[j][k] == 1 and e[i][k] == 1:
                        answer += 1
    return answer
