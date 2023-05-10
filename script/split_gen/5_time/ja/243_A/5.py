def main():
    v, a, b, c = map(int, input().split())
    while True:
        if v - a < 0:
            print('T')
            break
        else:
            v -= a
        if v - b < 0:
            print('F')
            break
        else:
            v -= b
        if v - c < 0:
            print('M')
            break
        else:
            v -= c
