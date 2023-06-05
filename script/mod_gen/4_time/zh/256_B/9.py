def problem256_b(n, a):
    p = 0
    for i in a:
        p += i // 4
    print(p)

if __name__ == '__main__':
    problem256_b()