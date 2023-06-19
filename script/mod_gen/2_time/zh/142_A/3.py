def problems142_a():
    N = int(input())
    if N % 2 == 0:
        print(0.5)
    else:
        print((N + 1) / (2 * N))

if __name__ == '__main__':
    problems142_a()