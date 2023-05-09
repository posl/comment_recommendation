def main():
    k = int(input())
    h = 21
    m = 0
    if k < 60:
        m = k
    elif k >= 60:
        h = h + int(k / 60)
        m = k % 60
    print(str(h) + ':' + str(m).zfill(2))
