def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(C/(B-A))
    else:
        print(0.0)
