def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        h1 = h // 10
        h2 = h % 10
        m1 = m // 10
        m2 = m % 10
        if h1 == m2 and h2 == m1:
            print(h, m)
            break
