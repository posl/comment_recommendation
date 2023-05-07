def main():
    A, B = map(int, input().split())
    if B >= 40:
        print(A ** 0.5)
        return
    if A == 1:
        print(1)
        return
    if A <= B:
        print(2)
        return
    g = 1
    t = 0
    while True:
        t += 1
        g += 1
        if t * B + ((A) / (g ** 0.5)) <= t * B + ((A) / ((g + 1) ** 0.5)):
            print(t * B + ((A) / (g ** 0.5)))
            return
