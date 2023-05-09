def problem():
    # Get input
    a, b = map(int, input().split())
    # Solve problem
    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    else:
        print('Alloy')

if __name__ == '__main__':
    problem()