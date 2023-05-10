def exchange(x):
    # 500円玉
    a = x // 500
    x -= a * 500
    # 100円玉
    b = x // 100
    x -= b * 100
    # 50円玉
    c = x // 50
    x -= c * 50
    # 10円玉
    d = x // 10
    x -= d * 10
    # 5円玉
    e = x // 5
    x -= e * 5
    # 1円玉
    f = x // 1
    x -= f * 1
    return 1000 * a + 5 * e
