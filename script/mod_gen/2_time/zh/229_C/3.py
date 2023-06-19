def get_max_cheese(n, w, cheese):
    cheese = sorted(cheese, key=lambda x: x[0] / x[1], reverse=True)
    sum = 0
    for i in range(n):
        if w >= cheese[i][1]:
            w -= cheese[i][1]
            sum += cheese[i][0]
        else:
            sum += cheese[i][0] * w / cheese[i][1]
            break
    return sum

if __name__ == '__main__':
    get_max_cheese()