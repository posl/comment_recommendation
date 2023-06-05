def main():
    a, b, c = map(int, input().split())
    if a == b != c or b == c != a or c == a != b:
        print('是')
    else:
        print('否')
