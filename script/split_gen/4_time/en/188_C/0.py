def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A = [max(A[2*j], A[2*j+1]) for j in range(2**(N-i-1))]
    print(A.index(min(A))+1)
