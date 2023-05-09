def count_inspectors(N, D):
    inspectors = 0
    for i in range(N):
        if i % (2 * D + 1) == 0:
            inspectors += 1
    return inspectors

if __name__ == '__main__':
    count_inspectors()