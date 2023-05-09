def problem():
    K = int(input())
    print(21 + (K + 9) // 60, (K + 9) % 60, sep=':')
