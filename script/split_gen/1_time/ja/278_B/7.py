def main():
    h, m = map(int, input().split())
    if m >= 10:
        h += 1
    if h >= 24:
        h -= 24
    print(h, 0)
