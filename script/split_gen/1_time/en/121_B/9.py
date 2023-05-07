def main():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum([1 for a in A if sum([a[i] * B[i] for i in range(M)]) + C > 0]))
