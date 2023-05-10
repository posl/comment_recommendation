def problem155_a():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif a == c and c != b:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem155_a()