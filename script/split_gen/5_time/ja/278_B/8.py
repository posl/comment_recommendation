def main():
    h,m = map(int,input().split())
    if m == 0:
        h += 1
        m = 0
    elif m <= 3:
        m = 0
    elif m <= 13:
        m = 10
    elif m <= 23:
        m = 20
    elif m <= 33:
        m = 30
    elif m <= 43:
        m = 40
    elif m <= 53:
        m = 50
    else:
        h += 1
        m = 0
    if h == 24:
        h = 0
    print(str(h).zfill(2) + " " + str(m).zfill(2))
