def main():
    k = int(input())
    hh = 21
    mm = 0
    mm += k
    if mm >= 60:
        hh += 1
        mm -= 60
    if hh >= 24:
        hh -= 24
    print("{:02d}:{:02d}".format(hh, mm))
