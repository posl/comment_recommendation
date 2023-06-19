def problem164_a():
    s, w = map(int, input().split())
    if s > w:
        print('安全')
    else:
        print('不安全')
