def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A > t:
        t += B
        g += 1
        t += A / (g ** (1/2))
    print(t - B)
