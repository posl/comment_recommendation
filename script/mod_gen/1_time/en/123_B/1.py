def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10) - max(A, B, C, D, E))

if __name__ == '__main__':
    main()