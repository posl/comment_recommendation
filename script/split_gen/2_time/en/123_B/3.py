def main():
    A, B, C, D, E = (int(input()) for _ in range(5))
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 4) + max(A % 10, B % 10, C % 10, D % 10, E % 10))
