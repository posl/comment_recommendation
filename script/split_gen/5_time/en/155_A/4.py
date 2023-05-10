def main():
    a, b, c = list(map(int, input().split()))
    if a == b and b != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    elif b == c and a != c:
        print('Yes')
    else:
        print('No')
