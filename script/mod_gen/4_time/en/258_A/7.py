def problem():
    K = int(input())
    print(21 + (K + 9) // 60, (K + 9) % 60, sep=':')

if __name__ == '__main__':
    problem()