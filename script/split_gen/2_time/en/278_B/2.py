def main():
    h, m = map(int, input().split())
    if m == 59:
        h = (h + 1) % 24
    m = (m + 1) % 60
    while not (h % 10 == m // 10 and h // 10 == m % 10):
        if m == 59:
            h = (h + 1) % 24
        m = (m + 1) % 60
    print(h, m)
