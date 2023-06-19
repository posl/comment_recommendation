def problem():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')

if __name__ == '__main__':
    problem()