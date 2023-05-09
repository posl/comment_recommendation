def main():
    N, X = map(int, input().split())
    X -= 1
    print(chr(X // N + ord('A')))
