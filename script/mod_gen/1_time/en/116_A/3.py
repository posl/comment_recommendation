def main():
    a, b, c = map(int, input().split())
    print((a * b * c) // (4 * (a * b + b * c + c * a)**0.5))

if __name__ == '__main__':
    main()