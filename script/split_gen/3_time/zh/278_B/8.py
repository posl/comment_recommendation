def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        if h // 10 == m % 10 and h % 10 == m // 10:
            break
    print(h, m)
