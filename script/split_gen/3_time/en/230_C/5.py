def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    L = Q - P + 1
    W = S - R + 1
    A -= 1
    B -= 1
    R -= 1
    S -= 1
    for i in range(L):
        for j in range(W):
            if (P + i - 1) % 2 == (R + j - 1) % 2:
                if (P + i - 1 - A) % 2 == (R + j - 1 - B) % 2:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (P + i - 1 - A) % 2 == (R + j - 1 - B) % 2:
                    print(".", end="")
                else:
                    print("#", end="")
        print()
