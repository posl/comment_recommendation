def main():
    N = int(input())
    a = 0
    b = 0
    while True:
        if N <= a**3 + a**2 * b + a * b**2 + b**3:
            print(a**3 + a**2 * b + a * b**2 + b**3)
            break
        if b == 0:
            a += 1
        else:
            b = 0
            a += 1
        if a == 1000:
            print(1000000000000000000)
            break
