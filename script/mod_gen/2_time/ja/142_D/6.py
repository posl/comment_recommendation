def main():
    from math import gcd
    a, b = map(int, input().split())
    g = gcd(a, b)
    print(len([i for i in range(1, g + 1) if g % i == 0]))

if __name__ == '__main__':
    main()