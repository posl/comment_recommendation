Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    for i in range(M):
        A[i] -= 1
        B[i] -= 1
    #print(N, M)
    #print(A)
    #print(B)
    #print(C)
    #print()
    #print()
    #print()
    #print()
