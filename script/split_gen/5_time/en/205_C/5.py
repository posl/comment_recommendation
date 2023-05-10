def main():
    a, b, c = map(int, input().split())
    if a < 0 and b < 0 and c % 2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print('=')
    elif a < b:
        print('<')
    else:
        print('>')
