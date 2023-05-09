def main():
    A, B, C, D = map(int, input().split())
    print(B - A + 1 - (B // C - (A - 1) // C) - (B // D - (A - 1) // D) + (B // lcm(C, D) - (A - 1) // lcm(C, D)))
