def count_biscuits(a, b, t):
    total_biscuits = 0
    for i in range(1, 1000000000):
        if a * i > t + 0.5:
            break
        total_biscuits += b
    return total_biscuits

if __name__ == '__main__':
    count_biscuits()