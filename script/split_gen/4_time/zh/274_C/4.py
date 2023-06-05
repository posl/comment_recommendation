def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = i
        while j > 1:
            j = j // 2
            B[i] += 1
    for i in range(1, 2*N+1):
        print(B[i])
