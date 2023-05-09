def main():
    a, b, c, d = map(int, input().split())
    if a <= b * d:
        print(-1)
    else:
        for i in range(1, 10 ** 5):
            if a <= (b * i) * (c * i):
                print(i)
                break
