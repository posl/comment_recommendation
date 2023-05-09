def main():
    N = int(input())
    A, B, C, D, E = map(int, input().split())
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)
