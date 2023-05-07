def main():
    h, m = map(int, input().split())
    if m % 10 == 0:
        h = (h + 1) % 24
        m = 0
    else:
        m = m + 10 - m % 10
    print(h, m)
