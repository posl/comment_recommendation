def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    score = 0
    for i in range(N):
        score += B[A[i]-1]
        if i < N-1 and A[i] == A[i+1] - 1:
            score += C[A[i]-1]
    print(score)
