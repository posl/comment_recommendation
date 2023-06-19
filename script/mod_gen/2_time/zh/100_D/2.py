def get_max_value(n, m, cakes):
    #美丽度
    beauty = [x for x, y, z in cakes]
    #美味度
    flavor = [y for x, y, z in cakes]
    #受欢迎度
    popular = [z for x, y, z in cakes]
    #总美丽度的绝对值
    beauty_abs = [abs(x) for x in beauty]
    #总美味度的绝对值
    flavor_abs = [abs(y) for y in flavor]
    #总受欢迎度的绝对值
    popular_abs = [abs(z) for z in popular]
    #总美丽度的绝对值+总美味度的绝对值+总受欢迎度的绝对值
    max_value = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                value = sum(beauty_abs[i:j+1]) + sum(flavor_abs[i:j+1]) + sum(popular_abs[i:j+1])
                if value > max_value:
                    max_value = value
    return max_value

if __name__ == '__main__':
    get_max_value()