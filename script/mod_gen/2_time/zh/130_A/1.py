def compare(X, A):
    if X < A:
        print(0)
    else:
        print(10)
X, A = map(int, input().split())
compare(X, A)
