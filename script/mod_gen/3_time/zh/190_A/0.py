def problem190_a(a, b, c):
    if c == 0:
        if a > b:
            return 'Takahashi'
        else:
            return 'Aoki'
    else:
        if b > a:
            return 'Aoki'
        else:
            return 'Takahashi'

if __name__ == '__main__':
    problem190_a()