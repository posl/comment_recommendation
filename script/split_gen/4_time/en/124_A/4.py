def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A, B) * 2 - 1)
