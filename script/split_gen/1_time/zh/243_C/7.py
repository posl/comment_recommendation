def check_collision(s, n, x, y):
    for i in range(n):
        if s[i] == 'L':
            x[i] = -x[i]
        else:
            y[i] = -y[i]
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                return True
    return False
