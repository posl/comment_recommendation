def main():
    A, B, C, D = map(int, input().split())
    import math
    def lcm(x, y):
        return (x * y) // math.gcd(x, y)
    def f(x):
        return x - (x // C + x // D - x // lcm(C, D))
    print(f(B) - f(A - 1))

if __name__ == '__main__':
    main()