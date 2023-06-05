def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    for a in range(1, 100000):
        for b in range(1, 100000):
            if n <= a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3:
                print(a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3)
                return
