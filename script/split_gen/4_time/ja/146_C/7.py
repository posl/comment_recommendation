def main():
    a, b, x = [int(i) for i in input().split()]
    n = 0
    for i in range(1,10):
        if x >= a * (10 ** i) + b * i:
            n = 10 ** i
    if n == 0:
        print(0)
    else:
        print(min((x - b * len(str(n))) // a, n - 1))
