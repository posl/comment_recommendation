def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if N <= min(A,B,C,D,E):
        print(5)
    else:
        print(4 + (N + min(A,B,C,D,E) - 1) // min(A,B,C,D,E))
