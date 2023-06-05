def main():
    k = int(input())
    h = 21
    m = 0
    h += k // 60
    m += k % 60
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    print("{:02d}:{:02d}".format(h, m))
