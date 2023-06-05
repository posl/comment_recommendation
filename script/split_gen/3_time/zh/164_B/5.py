def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        a -= d
    print("是" if c <= 0 else "否")
