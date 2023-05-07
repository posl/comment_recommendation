def main():
    A, B, C, D = map(int, input().split())
    print("Yes" if (C + D - 1) // D <= (A + B - 1) // B else "No")
