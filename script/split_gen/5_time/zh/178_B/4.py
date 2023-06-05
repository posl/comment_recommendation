def main():
    a, b, c, d = map(int, input().split())
    x = [a, b]
    y = [c, d]
    print(max([i * j for i in x for j in y]))
