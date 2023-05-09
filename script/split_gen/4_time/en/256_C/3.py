def main():
    # h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h1, h2, h3, w1, w2, w3 = 3, 4, 6, 3, 3, 7
    # h1, h2, h3, w1, w2, w3 = 3, 4, 5, 6, 7, 8
    # h1, h2, h3, w1, w2, w3 = 5, 13, 10, 6, 13, 9
    # h1, h2, h3, w1, w2, w3 = 20, 25, 30, 22, 29, 24
    if h1 == w1 and h2 == w2 and h3 == w3:
        print(1)
        exit(0)
    if h1 + h2 + h3 != w1 + w2 + w3:
        print(0)
        exit(0)
    if h1 == w1 and h2 == w2:
        print(1)
        exit(0)
    if h1 == w1 and h3 == w3:
        print(1)
        exit(0)
    if h2 == w2 and h3 == w3:
        print(1)
        exit(0)
    if h1 == w2 and h2 == w1:
        print(1)
        exit(0)
    if h1 == w3 and h3 == w1:
        print(1)
        exit(0)
    if h2 == w3 and h3 == w2:
        print(1)
        exit(0)
    print(0)
