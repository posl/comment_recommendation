def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        if i % 2 == 1:
            X -= a - 1
        else:
            X -= a
    if X >= 0:
        print("Yes")
    else:
        print("No")
