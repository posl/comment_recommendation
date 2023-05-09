def main():
    N, X = map(int, input().split())
    print(chr(X // N + 64 + X % N))
