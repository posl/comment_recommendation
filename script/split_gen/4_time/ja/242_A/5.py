def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
        return
    if A < X <= B:
        print(C / (B - A))
        return
    print(0.0)
