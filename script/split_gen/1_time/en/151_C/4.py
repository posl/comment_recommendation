def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if A[p] == 0:
            if s == 'AC':
                A[p] = 1
            else:
                B[p] += 1
    AC = sum(A)
    WA = 0
    for i in range(N):
        if A[i] == 1:
            WA += B[i]
    print(AC, WA)
