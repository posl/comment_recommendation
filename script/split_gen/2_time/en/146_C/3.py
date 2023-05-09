def main():
    A, B, X = map(int, input().split())
    if A == B:
        print(X // A)
    elif A > B:
        if X >= A:
            print(X // A)
        else:
            print(0)
    else:
        # A < B
        if X >= A:
            print(X // A)
        else:
            print(0)
