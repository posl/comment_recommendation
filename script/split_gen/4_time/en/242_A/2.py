def main():
    A, B, C, X = map(int, input().split())
    if X < A:
        print(0)
    elif X >= A and X <= B:
        print(1 / (B - A + 1))
    elif X > B and X <= B + C:
        print(C / (B - A + 1))
    else:
        print(0)
