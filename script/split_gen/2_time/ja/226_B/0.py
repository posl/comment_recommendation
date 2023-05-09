def main():
    N = int(input())
    D = {}
    for i in range(N):
        L, *A = map(int, input().split())
        A = tuple(A)
        if A in D:
            D[A] += 1
        else:
            D[A] = 1
    print(len(D))
