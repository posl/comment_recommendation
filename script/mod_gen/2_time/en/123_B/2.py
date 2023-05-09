def main():
    A, B, C, D, E = map(int, input().split())
    print((A + 9) // 10 * 10 + (B + 9) // 10 * 10 + (C + 9) // 10 * 10 + (D + 9) // 10 * 10 + E)

if __name__ == '__main__':
    main()