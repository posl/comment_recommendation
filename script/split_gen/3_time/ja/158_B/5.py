def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    elif B == 0:
        print(A)
        return
    else:
        if A > B:
            A, B = B, A
        loop = N // (A + B)
        mod = N % (A + B)
        if mod > A:
            mod = A
        print(A * loop + mod)
