def main():
    a, b = map(int, input().split())
    if 1 <= a and a <= 10 and 1 <= b and b <= 10:
        print('Yes')
    else:
        print('No')
