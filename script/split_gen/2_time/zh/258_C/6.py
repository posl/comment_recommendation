def get_max_number(grid):
    N = len(grid)
    max_number = 0
    for i in range(N):
        for j in range(N):
            # 从（i,j）开始，向右走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[i][(j + k) % N]
            max_number = max(max_number, number)
            # 从（i,j）开始，向下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][j]
            max_number = max(max_number, number)
            # 从（i,j）开始，向右下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][(j + k) % N]
            max_number = max(max_number, number)
            # 从（i,j）开始，向左下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][(j - k) % N]
            max_number = max(max_number, number)
    return max_number
