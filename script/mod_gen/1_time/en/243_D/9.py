def calc_vertice(n, x, s):
    current_vertice = x
    for i in range(n):
        if s[i] == 'U':
            current_vertice = current_vertice // 2
        elif s[i] == 'L':
            current_vertice = current_vertice * 2 - 1
        elif s[i] == 'R':
            current_vertice = current_vertice * 2 + 1
    return current_vertice

if __name__ == '__main__':
    calc_vertice()