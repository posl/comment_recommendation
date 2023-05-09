def solve():
    A, B, C, D, E = map(int, input().split())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 5))
