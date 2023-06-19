def problem257_a(n, x):
    return chr((x - 1) % 26 + ord('A'))

if __name__ == '__main__':
    problem257_a()