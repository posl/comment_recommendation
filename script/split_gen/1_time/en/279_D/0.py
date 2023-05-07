def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A > g**2:
        g += 1
        t += B
    t += A**0.5
    print(t)
