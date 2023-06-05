def problem177_a():
    D, T, S = map(int, input().split())
    if D <= T * S:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem177_a()