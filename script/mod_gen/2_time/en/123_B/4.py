def main():
    A, B, C, D, E = map(int, open(0).read().split())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10) - max(A % 10, B % 10, C % 10, D % 10, E % 10))

if __name__ == '__main__':
    main()