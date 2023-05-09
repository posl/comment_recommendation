def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum(1 for i in A if sum(a*b for a, b in zip(A[i], B)) + C > 0))
