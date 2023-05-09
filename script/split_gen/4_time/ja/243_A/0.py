def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print('T')
            return
        v -= b
        if v <= 0:
            print('M')
            return
        v -= c
        if v <= 0:
            print('F')
            return
