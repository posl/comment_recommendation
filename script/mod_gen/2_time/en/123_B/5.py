def main():
    A, B, C, D, E = map(int, [input() for _ in range(5)])
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 5) + max(A % 10, B % 10, C % 10, D % 10, E % 10))

if __name__ == '__main__':
    main()