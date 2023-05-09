def main():
    h, m = map(int, input().split())
    h2 = m // 10
    h1 = m % 10
    m2 = h // 10
    m1 = h % 10
    if h2 == 0:
        h2 = 10
    if m2 == 0:
        m2 = 10
    h3 = m1 * 10 + m2
    m3 = h1 * 10 + h2
    if h3 <= 23 and m3 <= 59:
        print(h3, m3)
    else:
        print(h2, m2)
