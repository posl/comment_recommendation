def main():
    N, A, B = map(int, input().split())
    n = N // (A + B)
    r = N % (A + B)
    print(n * A + min(r, A))
