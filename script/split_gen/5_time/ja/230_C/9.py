def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    if A > B:
        A, B = B, A
    if P > R:
        P, R = R, P
    if Q > S:
        Q, S = S, Q
    if (P > A and P > B) or (Q < A and Q < B) or (R > A and R > B) or (S < A and S < B):
        for i in range(Q - P + 1):
            print("." * (S - R + 1))
    else:
        for i in range(Q - P + 1):
            for j in range(S - R + 1):
                if (P + i + R + j) % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
