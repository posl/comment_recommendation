def main():
    # A, B = [int(i) for i in input().split()]
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)
