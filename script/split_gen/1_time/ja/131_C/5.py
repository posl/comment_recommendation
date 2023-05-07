def main():
    A, B, C, D = map(int, input().split())
    E = C * D
    F = B // C - (A - 1) // C
    G = B // D - (A - 1) // D
    H = B // E - (A - 1) // E
    ans = B - A + 1 - (F + G - H)
    print(ans)
