def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_t = min(A, B, C, D, E)
    print(-(-N // min_t) + 4)
