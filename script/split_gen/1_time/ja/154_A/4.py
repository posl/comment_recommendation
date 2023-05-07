def main():
    # input
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    # compute
    if U == S:
        A -= 1
    else:
        B -= 1
    # output
    print(A, B)
