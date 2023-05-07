def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(max([frozenset([i, j]) for i in range(N) for j in range(N)], key=lambda x: sum([A[i][j] for i, j in x])))
