def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    for a in A:
        if a == max_a:
            print(max(A[:A.index(a)] + A[A.index(a) + 1:]))
        else:
            print(max_a)
