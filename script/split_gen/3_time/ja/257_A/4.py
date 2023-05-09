def main():
    N, X = map(int, input().split())
    print(chr(X % 26 + 64))
