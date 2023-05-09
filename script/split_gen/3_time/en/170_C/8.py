def get_nearest_number(x, n, p):
    if n == 0:
        return x
    else:
        # 1 <= p_i <= 100
        # 1 <= X <= 100
        # 0 <= N <= 100
        # so, 0 <= d <= 200
        d = 200
        for i in range(1, 101):
            if i not in p:
                if abs(x - i) < d:
                    d = abs(x - i)
                    nearest_number = i
        return nearest_number
