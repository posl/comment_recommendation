def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    A = [[A[i][j] for i in range(2*N)] for j in range(M)]
    A = [[0 for _ in range(2*N)] for _ in range(M)] + A
    for i in range(M-1, -1, -1):
        for j in range(N):
            a = A[i][2*j]
            b = A[i][2*j+1]
            if (a == 'G' and b == 'C') or (a == 'C' and b == 'P') or (a == 'P' and b == 'G'):
                A[i-1][2*j] += 1
            elif (a == 'C' and b == 'G') or (a == 'P' and b == 'C') or (a == 'G' and b == 'P'):
                A[i-1][2*j+1] += 1
            else:
                A[i-1][2*j] += 0.5
                A[i-1][2*j+1] += 0.5
    A = A[0]
    A = [(A[i], i+1) for i in range(2*N)]
    A.sort()
    A = [x[1] for x in A]
    A.reverse()
    for i in range(2*N):
        print(A[i])
