def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum(1 for a in A if sum(b * c for b, c in zip(B, a)) + C > 0))
