def main():
    v, a, b, c = map(int, input().split())
    if a >= b and a >= c:
        print('F')
    elif b >= c:
        print('M')
    else:
        print('T')
