def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[0:P-1] + A[Q:R-1] + A[S-1:N]
    print(*B)
