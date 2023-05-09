def main():
    a, b = map(int, input().split())
    if 6*a >= b and a <= b:
        print('Yes')
    else:
        print('No')
