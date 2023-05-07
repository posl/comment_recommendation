def solve():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (i + j) % 2 == 0:
                if (i - A) * (i - A) + (j - B) * (j - B) <= (N - A) * (N - A) + (N - B) * (N - B):
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (i - A) * (i - A) + (j - B) * (j - B) <= (A - 1) * (A - 1) + (B - 1) * (B - 1):
                    print("#", end="")
                else:
                    print(".", end="")
        print()
