def main():
    k = int(input())
    h = 0
    m = 0
    if k >= 60:
        h = k // 60
        m = k % 60
    else:
        m = k
    print("%02d:%02d" % (h + 21, m))
