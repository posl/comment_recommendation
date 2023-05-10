def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    satisfaction = 0
    satisfaction += B[A[0]-1]
    for i in range(N-1):
        satisfaction += B[A[i+1]-1]
        if A[i+1] - A[i] == 1:
            satisfaction += C[A[i]-1]
    print(satisfaction)
