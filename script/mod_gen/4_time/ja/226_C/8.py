def max_time_to_learn(n, a):
    m = 0
    for i in range(n):
        if len(a[i]) == 0:
            m = max(m, 0)
        else:
            m = max(m, max(a[i]))
    return m

if __name__ == '__main__':
    max_time_to_learn()