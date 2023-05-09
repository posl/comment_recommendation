def main():
    N = int(input())
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print(-(-N // min(A, B, C, D, E)) + 4)
