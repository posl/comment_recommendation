def main():
    N, A, B = map(int, input().split())
    print((N // A) * (A * (A - 1) // 2) + (N // B) * (B * (B - 1) // 2) - (N // (A * B)) * (A * B * (A * B - 1) // 2))
