def main():
    v,a,b,c = map(int,input().split())
    while v > 0:
        if a > 0:
            v -= a
            if v < 0:
                print('F')
                break
        if b > 0:
            v -= b
            if v < 0:
                print('M')
                break
        if c > 0:
            v -= c
            if v < 0:
                print('T')
                break
