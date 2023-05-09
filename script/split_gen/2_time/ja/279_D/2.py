def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while g <= A:
        g += 1
        t += B
    print(t + A / (g ** 0.5))
