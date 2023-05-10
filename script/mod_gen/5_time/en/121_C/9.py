def min_cost(n, m, a_b):
    a_b = sorted(a_b, key=lambda x: x[0])
    cost = 0
    for a, b in a_b:
        if m <= b:
            cost += m * a
            break
        else:
            cost += a * b
            m -= b
    return cost

if __name__ == '__main__':
    min_cost()