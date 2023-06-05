def count_steps(n, m, a):
    steps = [0] * (n + 1)
    steps[0] = 1
    steps[1] = 1
    for i in range(2, n + 1):
        if i in a:
            steps[i] = 0
        else:
            steps[i] = (steps[i - 1] + steps[i - 2]) % 1000000007
    return steps[n]
