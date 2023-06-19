def problems258_a():
    k = int(input())
    h = int(k / 60)
    m = k - h * 60
    print("%02d:%02d" % (h + 21, m))

if __name__ == '__main__':
    problems258_a()