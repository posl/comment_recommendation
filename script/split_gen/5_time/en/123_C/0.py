def main():
    # input
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # compute
    # output
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)
