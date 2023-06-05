def main():
    x, k = map(int, input().split())
    for i in range(k):
        x = (x + 10 ** i) // (10 ** i) * (10 ** i)
    print(x)
