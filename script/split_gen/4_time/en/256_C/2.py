def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    if (h1 + h2 + h3) != (w1 + w2 + w3):
        print(0)
    else:
        print(1)
