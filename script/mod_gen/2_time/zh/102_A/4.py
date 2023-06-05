def problems102_a(n):
    i = 1
    while True:
        if i % n == 0 and i % 2 == 0:
            return i
        else:
            i += 1

if __name__ == '__main__':
    problems102_a()