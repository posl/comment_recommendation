def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print((A + 9) // 10 * 10 + (B + 9) // 10 * 10 + (C + 9) // 10 * 10 + (D + 9) // 10 * 10 + E - max(A, B, C, D, E) + 9)
