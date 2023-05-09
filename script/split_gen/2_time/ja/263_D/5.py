def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    A = [min(L, R)] * N
    print(sumA - sum(A))
