def main():
    A, B, C, D, E = map(int, open(0).read().split())
    print((A - 1) // 10 * 10 + A + (B - 1) // 10 * 10 + B + (C - 1) // 10 * 10 + C + (D - 1) // 10 * 10 + D + (E - 1) // 10 * 10 + E)

if __name__ == '__main__':
    main()