def calc_apple_pie_score(n, l, i):
    total = 0
    for j in range(n):
        if j != i:
            total += l + j
    return total

if __name__ == '__main__':
    calc_apple_pie_score()