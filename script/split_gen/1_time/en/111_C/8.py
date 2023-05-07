def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [A[i] for i in range(0, len(A), 2)]
    C = [A[i] for i in range(1, len(A), 2)]
    from collections import Counter
    B = Counter(B)
    C = Counter(C)
    B = B.most_common()
    C = C.most_common()
    if B[0][0] != C[0][0]:
        print(N - B[0][1] - C[0][1])
    else:
        if len(B) == 1:
            print(N - C[1][1])
        elif len(C) == 1:
            print(N - B[1][1])
        else:
            print(N - max(B[0][1] + C[1][1], B[1][1] + C[0][1]))
