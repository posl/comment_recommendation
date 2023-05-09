def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B)
    else:
        print(A * (B - 1) // B)
