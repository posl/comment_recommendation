def main():
    A, B, N = map(int, input().split())
    print(A * (N % B) // B)
