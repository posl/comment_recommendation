def main():
    N, X = map(int, input().split())
    A = ord("A")
    print(chr(A + (X-1) % N))
