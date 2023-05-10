def main():
    A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(A)
    elif A == B:
        print(A)
    else:
        print(3 - A - B)
