def main():
    a, b, c = map(int, input().split())
    if b > a and b < c:
        print('Yes')
    elif b < a and b > c:
        print('Yes')
    else:
        print('No')
