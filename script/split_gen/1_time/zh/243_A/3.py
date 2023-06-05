def main():
    v,a,b,c = map(int, input().split())
    while v >= 0:
        if v >= c:
            v -= c
        else:
            print('T')
            break
        if v >= b:
            v -= b
        else:
            print('F')
            break
        if v >= a:
            v -= a
        else:
            print('M')
            break
