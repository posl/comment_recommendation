def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B)
        return
    else:
        print(A * (B - 1) // B)
        return
