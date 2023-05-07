def main():
    A, B, X = map(int, input().split())
    if X >= A * 10**9 + B * 10:
        print(10**9)
        return
    if X < A + B:
        print(0)
        return
    if A > B:
        print(X // A)
        return
    if A <= B:
        print((X - B * 10) // (A - B))
        return
